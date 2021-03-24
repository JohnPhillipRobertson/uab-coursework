from flask import Flask, redirect, request, render_template, url_for, flash
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    grade = db.Column(db.Integer)

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        flash("I have been created")

    def __repr__(self):
        return "Student {}, number {}, got {} on the midterm.".format(self.name, self.id, self.grade)

###########################################################################


student_data = [None]


@app.route('/')
def index():
    flash("index() has executed")
    return render_template('home.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    flash("results has executed")
    return render_template("results.html", student_data=student_data)

###########################################################################


@app.route('/create', methods=['GET', 'POST'])
def create():
    flash("create has executed")
    if request.method == 'POST':
        name = request.args.get('name')
        grade = request.args.get('grade')
        stdnt = Student(name, grade)
        db.session.add(stdnt)
        db.session.commit()
        flash(stdnt)
        return redirect(url_for('home'))
    else:
        return render_template('home.html')


@app.route('/allstudents', methods=['GET', 'POST'])
def all_student():
    all_s = Student.query.all()
    student_data = all_s
    flash("all_student has executed")
    return redirect(url_for('results'))


@app.route('/goodstudents', methods=['GET', 'POST'])
def good_student():
    _ = Student.query.filter(Student.grade > 85)
    good_s = _.all()
    student_data = good_s
    flash("good_student has executed")
    return redirect(url_for('results'))


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id = request.form['id_del']
    stdnt = Student.query.get(id)
    db.session.delete(stdnt)
    db.session.commit()
    flash("delete has executed")
    return redirect(url_for('home'))

# https://stackoverflow.com/questions/50863789/in-flask-how-can-i-modify-html-with-code-in-python
# https://opentechschool.github.io/python-flask/core/form-submission.html
# https://stackoverflow.com/a/20689328/9295513
# https://stackoverflow.com/a/39024612/9295513


app.secret_key = "f"
if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)
