from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="employees_db"
        # cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    conn.close()
    return jsonify(employees)

@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE empId=%s", (emp_id,))
    employee = cursor.fetchone()
    conn.close()
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404


@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (empId, firstName, lastName, dateOfJoining) VALUES (%s, %s, %s, %s)",
        (data["empId"], data["firstName"], data["lastName"], data["dateOfJoining"])
    )
    conn.commit()
    conn.close()
    return jsonify(data), 201

@app.route('/employees/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET firstName=%s, lastName=%s, dateOfJoining=%s WHERE empId=%s",
        (data["firstName"], data["lastName"], data["dateOfJoining"], emp_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": f"Employee {emp_id} updated"})



@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE empId=%s", (emp_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Employee {emp_id} deleted"}), 200

@app.route('/innerjoin', methods=['GET'])
def inner_join():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.empId, e.firstName, e.lastName, d.deptName
        FROM employees e
        INNER JOIN departments d ON e.deptId = d.deptId
    """)
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

# LEFT JOIN: all employees, even if no department
@app.route('/leftjoin', methods=['GET'])
def left_join():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.empId, e.firstName, e.lastName, d.deptName
        FROM employees e
        LEFT JOIN departments d ON e.deptId = d.deptId
    """)
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

# RIGHT JOIN: all departments, even if no employees
@app.route('/rightjoin', methods=['GET'])
def right_join():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.empId, e.firstName, e.lastName, d.deptName
        FROM employees e
        RIGHT JOIN departments d ON e.deptId = d.deptId
    """)
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
