from flask import Flask, render_template, request, redirect, url_for
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

# Trang chính: danh sách sinh viên + form thêm
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student = Student(
            student_id=request.form['student_id'],
            name=request.form['name'],
            class_name=request.form['class_name']
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))

    query = request.args.get('query', '')
    if query:
        students = Student.query.filter(
            (Student.student_id.contains(query)) | (Student.name.contains(query))
        ).all()
    else:
        students = Student.query.all()

    return render_template('index.html', students=students)


# Sửa thông tin sinh viên
@app.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first_or_404()
    if request.method == 'POST':
        student.name = request.form['name']
        student.class_name = request.form['class_name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', student=student)

# Xóa sinh viên
@app.route('/delete/<student_id>', methods=['POST'])
def delete_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first_or_404()
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
