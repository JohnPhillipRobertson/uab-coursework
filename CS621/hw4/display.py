#!/usr/bin/env python
import cgitb
import cgi
import pymysql
cgitb.enable()
form = cgi.FieldStorage()

my_con = pymysql.connect(db='example', user='root',
                         passwd='password', host='localhost')
c = my_con.cursor()
c.execute("SELECT * FROM mytable")
recs = c.fetchall()

records1 = """
<html>
<body>
        <table>
                <tbody>
                        <tr>
                                <th>Company Name</th>
                                <th>Email</th>
                                <th>Phone Number</th>
                                <th>Address</th>
                        </tr>"""
records_dyn = [
    f"<tr><td>{i[1]}</td><td>{i[2]}</td><td>{i[3]}</td><td>{i[4]}</td></tr>" for i in recs]
records2 = """
<form method="POST" action="http://localhost/index.py">
<input type="submit" value="Go Back">
</form>
                </body>
        </table>
</body>
</html>"""
print("Content-Type:text/html; charset=utf-8")
print()
for i in records1.split("\n"):
    print(i)
for i in records_dyn:
    print(i)
for i in records2.split("\n"):
    print(i)
