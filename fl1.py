from flask import Flask, request , jsonify
app = Flask(__name__)
#
# @app.route("/get-item",methods=["GET"])
# def get_item():
#     return "GET EXECUTED"
#
# @app.route("/create-item",methods=["POST"])
# def create_item():
#     return "POST EXECUTED"
#
# # @app.route("/update-item",methods=["PUT"])
# # def update_item():
# #     return "PUT EXECUTED"
#
#
# # @app.route("/delete-item",methods=["DELETE"])
# # def delete_item():
# #     return "DELETE EXECUTED"
#
# items= [ "Apple","Orange","Banana"]
# @app.route("/list-items",methods=["GET"])
# def list_items():
#     return jsonify(items)
#
# @app.route("/list-items",methods=["POST"])
# def add_item():
#     data=request.get_json()
#     it=data.get("item")
#     items.append(it)
#     return "Post Executed"
# @app.route("/list-items/<int:index>",methods=["PUT"])
# def update_item(index):
#     data=request.get_json()
#     it=data.get("item")
#     items[index] = it
#     return "Put Executed"
# @app.route("/list-items/<int:index>",methods=["DELETE"])
# def delete_item(index):
#     items.pop(index)
#     return "Delete Executed"
#
employees = [
    {"empId": 101, "firstName": "John", "lastName": "Doe", "dateOfJoining": "2022-05-10"},
    {"empId": 102, "firstName": "Jane", "lastName": "Smith", "dateOfJoining": "2023-01-15"}
]

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)


@app.route('/employees/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    employee = next((emp for emp in employees if emp["empId"] == emp_id), None)
    if employee:
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}),404


@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    employees.append(data)
    return jsonify(data), 201


@app.route('/employees/<int:emp_id>', methods=['PUT'])
def update_employee(emp_id):
    data = request.get_json()
    for emp in employees:
        if emp["empId"] == emp_id:
            emp.update(data)
            return jsonify(emp)
    return jsonify({"error": "Employee not found"}), 404

@app.route('/employees/<int:emp_id>', methods=['DELETE'])
def delete_employee(emp_id):
    for emp in employees:
        if emp["empId"] == emp_id:
            employees.remove(emp)
            break
    return jsonify({"message": f"Employee {emp_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

