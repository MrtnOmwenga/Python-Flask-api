# import modules
from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector
from flask.json import jsonify

#connect to database
db = mysql.connector.connect(host = "localhost", user = "root", password = "******.", database = "employees")
cursor = db.cursor()

app = Flask(__name__)
api = Api(app)

#Getting employee names
class Employees(Resource):
    def get(self):
        conn = db.connect() # connect to database
        cursor.execute("select NAME from employee_details") # query to get info.
        result = cursor.fetchall() #fetch data
        return result #show result

#getting specific employee names using id's
class Employees_from_id(Resource):
    def get(self,id):
        conn = db.connect()
        query = "SELECT NAME FROM employee_details WHERE ID = %d"%int(id)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

#getting employee names from a department
class Employees_from_department(Resource):
    def get(self, department):
        conn = db.connect()
        query = "SELECT NAME FROM employee_details WHERE DEPARTEMENT = %s"%department
        cursor.execute(query)
        result = cursor.fetchall()
        return result

#getting employee names from their address
class Employees_from_address(Resource):
    def get(self, address):
        conn = db.connect()
        query = "SELECT NAME FROM employee_details WHERE ADRESS = %s"%address
        cursor.execute(query)
        result = cursor.fetchall()
        return result

#getting department names from employee id
class Department(Resource):
    def get(self, id):
        conn = db.connect()
        query = "SELECT DEPARTEMENT FROM employee_details WHERE ID = %d"%int(id)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

#getting department names from employee id
class Position(Resource):
    def get(self, id):
        conn = db.connect()
        query = "SELECT POSITION FROM employee_details WHERE ID = %d"%int(id)
        cursor.execute(query)
        result = cursor.fetchall()
        return result

#getting employee id names from employee name
class id(Resource):
    def get(self, name):
        conn = db.connect()
        query = "SELECT ID FROM employee_details WHERE ID = %s"%name
        cursor.execute(query)
        result = cursor.fetchall()
        return result

#getting employee address from a employee id
class Address(Resource):
    def get(self, id):
        conn = db.connect() # connect to database
        query = "SELECT ADRESS FROM employee_details WHERE ID = %d"%int(id)
        cursor.execute(query) # This line performs query and returns json result
        result = cursor.fetchall()
        return result

#Add employees
@app.route("/add_Emplolyees", methods = ["POST"])
class add_Employees(Resource):
    def put(self,name, id, department, position, address):
        conn = db.connect() # connect to database
        print(request.json)
        name =  request.json['name']
        id = request.json['id']
        department = request.json['department']
        position = request.json['position']
        address = request.json['address']
        details = [name, id, department, position, address]
        cursor.execute("INSERT INTO  employees_details (NAME, ID, DEPARTEMENT, POSITION, ADRESS) values (%s, %s, %s, %s, %s)"%details) # query to get info.
        return {'status':'success'}
        
#Create routes
api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_from_id, '/employees_from_id/<id>') # Route_2
api.add_resource(Employees_from_department, '/employees_from_department/<department>') # Route_3
api.add_resource(Employees_from_address, '/employees_from_address/<address>') # Route_4
api.add_resource(Department, '/department/<id>') # Route_5
api.add_resource(Position, '/position/<id>') # Route_6
api.add_resource(id, '/id/<name>') # Route_8
api.add_resource(Address, '/address/<id>') # Route_9

#Run app
if __name__ == '__main__':
    app.run(port='5002')