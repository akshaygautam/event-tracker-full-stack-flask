from datetime import datetime
from app.db import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    marks = db.Column(db.Integer, nullable = False)
    city = db.Column(db.String, nullable = False)

    def __repr__(self) -> str:
        return f'Student = {self.name} marks = {self.marks} city = {self.city}'
    
    def __init__(self, name, marks, city) -> None:
        self.name  = name
        self.marks = marks
        self.city = city

    def as_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "marks": self.marks,
            "city" : self.city  
        }