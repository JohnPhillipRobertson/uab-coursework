#!/usr/bin/env python
import cgitb
import cgi
import pymysql

form = cgi.FieldStorage()
name = form.getvalue("name")
m1 = int(form.getvalue("mid_one"))
m2 = int(form.getvalue("mid_two"))
f = int(form.getvalue("fin_ex"))
avg = (m1+m2+f+f)/4

c = my_con.cursor()
sql = "INSERT INTO `example` (`name`, `avg`) VALUES (%s, %s)"
c.execute(sql, (name, avg))
c.commit()
c.close()

print("Content-Type:text/html; charset=utf-8")
print()
print("<html>")
print("<form method="POST" action="index.py">")
print("<input type="submit" value="Go Back">")
print("</form")
print("</html>")
