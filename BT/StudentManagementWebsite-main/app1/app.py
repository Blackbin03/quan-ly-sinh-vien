import os, sys
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

# add shared models path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared')))
from models import db, Student

app = Flask(__name__, template_folder='templates')
app.secret_key = 'dev-secret'
basedir = os.path.abspath(os.path.dirname(__file__))
# DB at project root
db_path = os.path.abspath(os.path.join(basedir, '..', 'students.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path.replace('\\', '/')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id','').strip()
        name = request.form.get('name','').strip()
        class_name = request.form.get('class_name','').strip()
        if not student_id or not name or not class_name:
            flash('Please fill all fields', 'danger')
            return redirect('/')
        # create
        s = Student(student_id=student_id, name=name, class_name=class_name)
        try:
            db.session.add(s)
            db.session.commit()
            flash('Student added', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error: ' + str(e), 'danger')
        return redirect('/')
    return render_template('add_student.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
