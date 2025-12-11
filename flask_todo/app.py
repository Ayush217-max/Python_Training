from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime, UTC

app = Flask(__name__)
app.secret_key = "supersecretkey"

# --- Database helper ---
def get_db_connection():
    conn = sqlite3.connect("todo.db")
    conn.row_factory = sqlite3.Row
    return conn

# --- Home page ---
@app.route("/")
def index():
    status_filter = request.args.get("status_filter")

    conn = get_db_connection()
    if status_filter:
        rows = conn.execute(
            "SELECT * FROM tasks WHERE status = ? ORDER BY created_at DESC",
            (status_filter,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM tasks ORDER BY created_at DESC"
        ).fetchall()
    conn.close()

    # Convert rows to dicts and parse created_at
    tasks = []
    for row in rows:
        task = dict(row)
        try:
            task["created_at"] = datetime.fromisoformat(task["created_at"])
        except Exception:
            task["created_at"] = task["created_at"]  # fallback if parsing fails
        tasks.append(task)

    # Counts for navbar badges
    conn = get_db_connection()
    counts = {
        "all": conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0],
        "pending": conn.execute("SELECT COUNT(*) FROM tasks WHERE status='Pending'").fetchone()[0],
        "completed": conn.execute("SELECT COUNT(*) FROM tasks WHERE status='Completed'").fetchone()[0],
    }
    conn.close()

    return render_template("index.html", tasks=tasks, counts=counts, status_filter=status_filter)

# --- Add a task ---
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form.get("description")
    created_at = datetime.now(UTC).isoformat()

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (title, description, status, created_at) VALUES (?, ?, ?, ?)",
        (title, description, "Pending", created_at)
    )
    conn.commit()
    conn.close()

    flash("Task added successfully!", "success")
    return redirect(url_for("index"))

# --- Mark task as completed ---
@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    flash("Task marked as completed!", "success")
    return redirect(url_for("index"))

# --- Edit task ---
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    conn = get_db_connection()
    task = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()

    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        status = request.form.get("status")
        conn.execute(
            "UPDATE tasks SET title=?, description=?, status=? WHERE id=?",
            (title, description, status, task_id)
        )
        conn.commit()
        conn.close()
        flash("Task updated successfully!", "info")
        return redirect(url_for("index"))

    # compute counts for navbar
    counts = {
        "all": conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0],
        "pending": conn.execute("SELECT COUNT(*) FROM tasks WHERE status='Pending'").fetchone()[0],
        "completed": conn.execute("SELECT COUNT(*) FROM tasks WHERE status='Completed'").fetchone()[0],
    }
    conn.close()

    return render_template("edit.html", task=task, counts=counts)


# --- Delete task ---
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    flash("Task deleted!", "danger")
    return redirect(url_for("index"))

# --- Initialize DB (run once) ---
def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
