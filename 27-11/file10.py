from datetime import datetime

log = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  Application started\n"

with open("app.log", "a") as file:
    file.write(log)

print("Log entry added!")
