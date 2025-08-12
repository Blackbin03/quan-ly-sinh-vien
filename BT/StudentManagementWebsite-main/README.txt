StudentManagementWebsite-fixed
-----------------------------

Structure:
- shared/models.py  (shared SQLAlchemy models)
- students.db       (SQLite database)
- app1/             (Add student app, port 5000)
- app2/             (Search student app, port 5001)

How to run:
1) (Optional) create venv and install requirements:
   python -m venv .venv
   .\.venv\Scripts\activate   (Windows)
   pip install -r requirements.txt

2) Run Add app (in one terminal):
   cd app1
   python app.py

3) Run Search app (in another terminal):
   cd app2
   python app.py

Notes:
- Database file is at: /mnt/data/StudentManagementWebsite-fixed/students.db
- If running on Windows and path issues appear, ensure Python can access the file and path separators are correct.
