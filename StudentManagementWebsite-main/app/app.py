from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Trang chủ - Danh sách sinh viên
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Thêm sinh viên
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        class_name = request.form['class_name']

        new_student = Student(student_id=student_id, name=name, class_name=class_name)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('form.html', action="Thêm", student=None)

# Sửa sinh viên
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.student_id = request.form['student_id']
        student.name = request.form['name']
        student.class_name = request.form['class_name']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('form.html', action="Sửa", student=student)

# Xóa sinh viên
@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
