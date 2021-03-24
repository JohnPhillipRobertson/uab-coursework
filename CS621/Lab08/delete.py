#!/usr/bin/env python
import cgitb
import cgi
import pymysql
form = cgi.FieldStorage()
name = form.getvalue("name")
c = my_con.cursor()
sql = "DELETE FROM `example` where name = `name`"
c.execute(sql, (name, avg))
c.commit()
c.close()
j = """
<form method="POST" action="index.py">
<input type="submit" value="Go Back">
</form>
"""
print("Content-Type:text/html; charset=utf-8")
print()
for i in j:
    print(j)
