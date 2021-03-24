#!/usr/bin/env python
import cgitb
import cgi
import pymysql
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
# https://pymysql.readthedocs.io/en/latest/user/examples.html

cgitb.enable()
name, avg = None, None


def saveButton():
    form = cgi.FieldStorage()
    global name, avg
    name = form.getvalue("name")
    m1 = form.getvalue("mid_one")
    m2 = form.getvalue("mid_two")
    f = form.getvalue("fin_ex")
    avg = (m1+m2+f+f)/4

	c = my_con.cursor()
    sql = "INSERT INTO `example` (`name`, `avg`) VALUES (%s, %s)"
    c.execute(sql, (name, avg))
    c.commit()
    c.execute("SELECT * FROM example")
    recs = c.fetchall()
    c.close()


records1 = """
<body>
	<table>
		<tbody>
			<tr>
				<th>Full Name</th>
				<th>Average Score</th>
			</tr>"""
records_dyn = [
    f"<tr><td>{name}</td><td>{avg}</td></tr>" for recs[1], recs[2] in recs]
records2 = """
<form method="POST" action="index.py">"
<input type="submit" value="Go Back">"
"</form"
		</body>
	</table>
</body>
</html>"""


def displayButton():
    print("Content-Type:text/html; charset=utf-8")
    print()
    c.execute("SELECT * FROM example")
    recs = c.fetchall()

    for i in records1.split("\n"):
        print(i)
    for i in records_dyn:
        print(i)
    for i in records21.split("\n"):
        print(i)


def deleteButton():
	form = cgi.FieldStorage()
	name = form.getvalue("name")

	c = my_con.cursor()
	sql = "DELETE FROM `example` where name = `name`"
	c.execute(sql, (name, avg))
    c.commit()
	c.close()
