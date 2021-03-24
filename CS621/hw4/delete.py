#!/usr/bin/env python
import cgitb
import cgi
import pymysql
cgitb.enable()
form = cgi.FieldStorage()
name = form.getfirst("phone_del")

my_con = pymysql.connect(db='example', user='root',
                         passwd='password', host='localhost')
c = my_con.cursor()
sql = "DELETE FROM `mytable` where name = `name`"
c.execute(sql, (name))
c.commit()
c.close()


j = """
<html>
<form method="POST" action="http://localhost/index.py">
<input type="submit" value="Go Back">
</form>
<h1>{}</h1>
</html>
""".format(name)
print("Content-Type:text/html; charset=utf-8")
print()
for i in j.split("\n"):
    print(i)
