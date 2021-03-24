from flask import *
import psycopg2
from weather import getTemp
import datetime

app = Flask(__name__)

def getConnection():
    conn = psycopg2.connect(database='postgres', user='Team6', password='6Team6', host='164.111.161.243' , port='5432')
    return conn

def getCursor(conn):
    return conn.cursor()

def CtoF(celcius):
    return int((celcius * 9/5) + 32)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/floor_plan')
def floorPlan():
    todayDate = str(datetime.datetime.now()).split()[0]
    hour = int(str(datetime.datetime.now()).split()[1][:2])
    outsideTemp = CtoF(getTemp(todayDate)[hour - 6 - 1])
    print(hour)
    return render_template('floor.html', outsideTemp=outsideTemp)

@app.route('/usage')
def usage():
    return render_template('graph.html')
if __name__=='__main__':
	app.run(debug=True)