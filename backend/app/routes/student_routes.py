from flask import request, jsonify, abort
from app.db import db
from app.models import Student

def init_student_routes(app):
    @app.route('/students', methods = ['POST'])
    def create_student():
        name = request.json.get('name')
        marks = request.json.get('marks')
        city = request.json.get('city')
    
        if not name or not marks or not city:
            abort(400, description="All Details are Required")

        student = Student(name, marks, city)
        db.session.add(student)
        db.session.commit()
        return jsonify(student.as_dict()), 201
    
    @app.route('/students', methods=['GET'])
    def get_all_students():
        students = Student.query.all()
        students_json = [student.as_dict() for student in students]
        return jsonify(students_json)

    @app.route('/students/<int:id>', methods = ['GET'])
    def student_by_id(id: int):
        student = Student.query.get(id)
        if student is None:
            abort(404, description=f"Student with ID {id} not found.")
        return jsonify(student.as_dict())
    
    @app.route('/students/<int:id>', methods = ['DELETE'])
    def delete_by_student(id: int):
        student = Student.query.get(id)
        if student is None:
            abort(404, description=f"Student with ID {id} not found.") 
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": f"Deleted Student (id: {id})"}), 204
    
    @app.route('/students/<int:id>', methods = ['PUT'])
    def update_student(id: int):
        student = Student.query.get(id)
        if student is None:
            abort(404, description=f"student with ID {id} not found.")
        
        if not request.json:
            abort(400, description="No JSON data provided.")

        if 'name' in request.json:
            student.name = request.json['name']
        if 'marks' in request.json:
            student.marks = request.json['marks']
        if 'city' in request.json:
            student.city = request.json['city']

        db.session.commit()
        return jsonify(student.as_dict())