""" Arpit Patel
The following code is to build a web page which will display the result of the final project """


import os
import sqlite3
from flask import Flask, render_template, redirect
from typing import Dict

app = Flask(__name__)

@app.route('/')
def index()   :
#Redirect index to students page
    return redirect('templates/students')

@app.route('/students')
def student_summary()   :
# Query for Students Grades
    db_path = "Testdb.db"

    try:
        db = sqlite3.connect(db_path)
    except sqlite3.OperationalError:
        return 404
    else:
        query = "select students.Name, students.CWID, grades.Course, grades.Grade, instructors.Name from students,grades,instructors where students.CWID=StudentCWID and InstructorCWID=instructors.CWID order by students.Name"
        data = [{'Name': name, 'CWID': cwid, 'Course': course, 'Grade': grade, 'Instructor': instructor} for name, cwid, course, grade, instructor in db.execute(query)]

        db.close()

        return render_template(
            'students.html',
                title = 'Stevens Repository',
                table_title = 'Students Summary',
                students = data)

app.run(debug=True)
