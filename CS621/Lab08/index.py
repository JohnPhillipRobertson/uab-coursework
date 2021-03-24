#!/usr/bin/env python
import cgitb
import cgi
import pymysql
my_con = pymysql.connect(db='example', user='root',
                         passwd='password', host='localhost')
c = my_con.cursor()
c.execute("TRUNCATE example")
c.commit()
c.close()
cgi.enable()
j = """
<html>
<body>
	<h1>Enter a new record</h1>
	<form method="POST" action="save.py">
		<label for="name">Full name :</label>
		<input type="text" id="name" name="name"><br>
		<label for="mid_one">Midterm #1:</label>
		<input type="number" id="mid_one" name="mid_one"><br>
		<label for="mid_two">Midterm #2:</label>
		<input type="number" id="mid_two" name="mid_two"><br>
		<label for="fin_ex">Final Exam:</label>
		<input type="number" id="fin_ex" name="fin_ex"><br>
		<input type="submit" value="Save">
	</form>
	<h1>Display the records</h1>
	<form method="POST" action="display.py">
		<label for="display"></label>
		<input type="submit" value="Display All">
	</form>
	<h1>Delete a record</h1>
	<form method="POST" action="delete.py">
		<label for="name">Full name :</label>
		<input type="text" id="name" name="name"><br>
		<input type="submit" value="Delete">
	</form>
</body>
</html>"""
for i in j.split("\n"):
    print(i)
