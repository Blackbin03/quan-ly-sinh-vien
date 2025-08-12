import os, sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared')))
from models import db, Student

app = Flask(__name__, template_folder='templates')
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.abspath(os.path.join(basedir, '..', 'students.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path.replace('\\', '/')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET'])
def search():
    q = request.args.get('q','').strip()
    if q:
        students = Student.query.filter((Student.student_id.contains(q)) | (Student.name.contains(q))).all()
    else:
        students = Student.query.limit(100).all()
    return render_template('search.html', students=students, q=q)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)
