from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(64), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    class_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.student_id} - {self.name}>"
