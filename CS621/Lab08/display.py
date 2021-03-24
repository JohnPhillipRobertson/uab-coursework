#!/usr/bin/env python
import cgitb
import cgi
import pymysql

form = cgi.FieldStorage()
c.execute("SELECT * FROM example")
recs = c.fetchall()
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
<form method="POST" action="index.py">
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
for i in records1.split("\n"):
    print(i)
