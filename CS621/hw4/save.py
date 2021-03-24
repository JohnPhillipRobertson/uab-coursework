#!/usr/bin/env python
import cgitb
import cgi
import pymysql

cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue("name")
mail = form.getvalue("mail")
phone = form.getvalue("phone")
address = form.getvalue("address")

my_con = pymysql.connect(db='example', user='root',
                         passwd='password', host='localhost')
c = my_con.cursor()
sql = "INSERT INTO `mytable` (`name`, `mail`, `phone`, `address`) VALUES (%s, %s, %s, %s)"
c.execute(sql, (name, mail, phone, address))
c.commit()
c.close()

print("Content-Type:text/html; charset=utf-8")
print()
print("<html>")
print('<form method="POST" action="http://localhost/index.py">')
print('<input type="submit" value="Go Back">')
print("</form")
print("</html>")
