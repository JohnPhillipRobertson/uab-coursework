#!/usr/bin/env python
"""
•The user should be able to add a new record
The company name, email, phone number and address will be required. Feel free to add other information
•The user should be able to display all of the records
•The user should be able to delete any record
You can put a delete option when you display the records, or the user can delete the company record by searching the phone number
•The user should be able to update the records
Similar to delete option, you can either allow user to update the record from the table, or user can search/find the record and update it
"""
import cgitb
import pymysql


my_con = pymysql.connect(db='example', user='root',
                         passwd='password', host='localhost')
c = my_con.cursor()
c.execute("TRUNCATE mytable")
c.commit()
c.close()

cgitb.enable()
html = """
<html>
<body>
        <h1>Enter a new record</h1>
        <form name="yp" method="POST" action="http://localhost/save.py">
                <label for="name"> Company name: </label>
                <input type="text" id="name" name="name"> <br>
                <label for="mail"> Email: </label>
                <input type="email" id="mail" name="mail"> <br>
                <label for="phone"> Phone Number, formatted as XXXXXXXXXX: </label>
                <input type="text" id="phone" name="phone"> <br>
                <label for="address"> Address: </label>
                <input type="text" id="address" name="address"> <br>

                <input type="submit" value="Add">
        </form>

        <h1>Display all records</h1>
        <form name="disp" method="POST" action="http://localhost/display.py">
                <input type="submit" value="Display all records">
        </form>

        <h1>Delete a record</h1>
        <form name="del" method="POST" action="http://localhost/delete.py">
                <label for="phone_del"> Phone number, formatted as above: </label>
                <input type="text" id="phone_del" name="phone_del"><br>

                <input type="submit" value="Delete">
        </form>

        <h1>Update a record</h1>
        <form name="upd" method="POST" action="http://localhost/update.py">
                <label for="name"> Company name: </label>
                <input type="text" id="name" name="name"> <br>
                <label for="mail"> Email: </label>
                <input type="email" id="mail" name="mail"> <br>
                <label for="phone"> Phone Number, formatted as XXXXXXXXXX: </label>
                <input type="text" id="phone" name="phone"> <br>
                <label for="address"> Address: </label>
                <input type="text" id="address" name="address"> <br>

                <input type="submit" value="Update">
        </form>
</body>
</html>"""
print("Content-Type:text/html; charset=utf-8")
print()
for i in html.split("\n"):
    print(i)
