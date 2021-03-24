from random import randint
import psycopg2
from weather import getTemp
import datetime
import random

def getConnection():
    conn = psycopg2.connect(database='postgres', user='Team6', password='6Team6', host='164.111.161.243' , port='5432')
    return conn

def getCursor(conn):
    return conn.cursor()

def addOctoberWeather():
    conn = getConnection()
    cur = getCursor(conn)
    cur.execute('''CREATE TABLE weather(date DATE, hourlyTemp NUMERIC [])''')
    dates = [f'2020-10-{i}' if len(str(i)) == 2 else f'2020-10-0{i}' for i in range(1, 32)]
    temps = []
    for date in dates:
        temps.append((date, getTemp(date)))
    for dates in temps:
        cur.execute("INSERT INTO weather (date, hourlyTemp) VALUES (%s, %s)",(dates[0], dates[1]))
    cur.execute("SELECT * FROM weather")
    # print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()

def addNovWeather():
    conn = getConnection()
    cur = getCursor(conn)
    dates = [f'2020-11-{i}' if len(str(i)) == 2 else f'2020-11-0{i}' for i in range(1, 13)]
    temps = []
    for date in dates:
        temps.append((date, getTemp(date)))
    for dates in temps:
        cur.execute("INSERT INTO weather (date, hourlyTemp) VALUES (%s, %s)",(dates[0], dates[1]))
    cur.execute("SELECT * FROM weather")
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()

def addRemainingNovWeather():
    conn = getConnection()
    cur = getCursor(conn)
    dates = [f'2020-11-{i}' if len(str(i)) == 2 else f'2020-11-0{i}' for i in range(13, 29)]
    temps = []
    for date in dates:
        temps.append((date, getTemp(date)))
    for dates in temps:
        cur.execute("INSERT INTO weather (date, hourlyTemp) VALUES (%s, %s)",(dates[0], dates[1]))
    cur.execute("SELECT * FROM weather")
    print(cur.fetchall())
    conn.commit()
    cur.close()
    conn.close()

def CtoF(celcius):
    return int((celcius * 9/5) + 32)

def changeInTemperature(time, minutesOpen, date, internalTemp):
    conn = getConnection()
    cur = getCursor(conn)
    date = date.split('-')
    time = time.split(':')
    startTime = datetime.datetime (int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]))
    cur.execute('SELECT hourlyTemp FROM weather WHERE date = %s', (datetime.date(int(date[0]), int(date[1]), int(date[2])), ))

def randomizeOctoberData(days, octBegin, dishwasherOnOct, laundryOnOct, oct):
    conn = getConnection()
    cur = getCursor(conn)
    execute = "INSERT INTO usageHistory (day, power, water, powerCost, waterCost, totalCost) VALUES (%s, %s, %s, %s, %s, %s)"
    for date in oct:
        day = days[(octBegin + int(date[-2:]) - 1) % 7]
        if day[0] == 'S':
            microwave = (30/60) * 1000 #watts
            stove = (30/60) * 3000 #watts
            oven = (60/60) * 1200 #watts
            livingRoomTV = 8 * 200 #watts
            bedroomTV = 4 * 200 #watts
            showerWater = 20 * 3 #gallons
            showerWaterHeater = (25 * .65 * 3 * 4)/60 * 4500 #watts
            bathWater = 36 * 3 #gallons
            bathWaterHeater = (30 * .65 * 3 * 4)/60 * 4500 #watts
        else: 
            microwave = (20/60) * 1000 #watts
            stove = (15/60) * 3000 #watts
            oven = (45/60) * 1200 #watts
            livingRoomTV = 4 * 200 #watts
            bedroomTV = 2 * 200 #watts
            showerWater = 20 * 2 #gallons
            showerWaterHeater = (25 * .65 * 2 * 4)/60 * 4500 #watts
            bathWater = 36 * 2 #gallons
            bathWaterHeater = (30 * .65 * 2 * 4)/60 * 4500 #watts
        if date in dishwasherOnOct:
            dishwasherWater = 7 #gallons
            dishwasher = (45/60) * 1350 # watts
            dishwasherWaterHeater = (6 * 4)/60 * 4500 #watts
        else:
            dishwasherWater = 0 #gallons
            dishwasher = 0 # watts
            dishwasherWaterHeater = 0 #watts
        if date in laundryOnOct:
            washerWater = 15 #gallons
            washer = (30/60) * 500 #watts
            washerWaterHeater = (20 * .85 * 4)/60 * 4500 #watts
            dryer = (30/60) * 3000 #watts
        else:
            washerWater = 0 #gallons
            washer = 0 #watts
            washerWaterHeater = 0 #watts
            dryer = 0 #watts

        refridgerator = 150 * 24 #watts
        lightsUsageHours = 0
        # lights = ['bedroom1_light1', 'bedroom1_light2', 'bedroom1_light3', 'bedroom2_light1', 'bedroom2_light2', 'bedroom2_light3', 'bedroom3_light1', 'bedroom3_light2', 'bedroom3_light3', 'kitchen_light', 'living_room_light1', 'living_room_light2', 'living_room_light3']
        for i in range(random.randint(4, 16)):
            lightsUsageHours += random.uniform(0, 7)
        lights = lightsUsageHours * 60

        bathExhaust = sum([random.uniform(0, 1) for i in range(random.randint(3, 12))]) * 30

        HVACon = random.uniform(60, 180) #minutes
        hvac = (HVACon/60) * 3500

        totalPower = microwave + stove + oven + livingRoomTV + bedroomTV + showerWaterHeater + bathWaterHeater + dishwasher + washer + refridgerator + lights + bathExhaust + hvac + dishwasherWaterHeater + washerWaterHeater + dryer
        totalWater = showerWater + bathWater + dishwasherWater + washerWater

        totalPowerCost = round(totalPower/1000 * 0.13, 2)
        totalWaterCost = totalWater * 0.0252

        print(totalPower)
        print(totalWater)
        print(totalPowerCost)
        print(totalWaterCost)
        cur.execute(execute, (date, totalPower, totalWater, totalPowerCost, totalWaterCost, totalPowerCost + totalWaterCost))

    conn.commit()
    cur.close()
    conn.close()

def randomizeNovData(days, novBegin, dishwasherOnNov, laundryOnNov, nov):
    conn = getConnection()
    cur = getCursor(conn)
    execute = "INSERT INTO usageHistory (day, power, water, powerCost, waterCost, totalCost) VALUES (%s, %s, %s, %s, %s, %s)"
    for date in nov:
        day = days[(novBegin + int(date[-2:]) - 1) % 7]
        if day[0] == 'S':
            microwave = (30/60) * 1000 #watts
            stove = (30/60) * 3000 #watts
            oven = (60/60) * 1200 #watts
            livingRoomTV = 8 * 200 #watts
            bedroomTV = 4 * 200 #watts
            showerWater = 20 * 3 #gallons
            showerWaterHeater = (25 * .65 * 3 * 4)/60 * 4500 #watts
            bathWater = 36 * 3 #gallons
            bathWaterHeater = (30 * .65 * 3 * 4)/60 * 4500 #watts
        else: 
            microwave = (20/60) * 1000 #watts
            stove = (15/60) * 3000 #watts
            oven = (45/60) * 1200 #watts
            livingRoomTV = 4 * 200 #watts
            bedroomTV = 2 * 200 #watts
            showerWater = 20 * 2 #gallons
            showerWaterHeater = (25 * .65 * 2 * 4)/60 * 4500 #watts
            bathWater = 36 * 2 #gallons
            bathWaterHeater = (30 * .65 * 2 * 4)/60 * 4500 #watts
        if date in dishwasherOnNov:
            dishwasherWater = 7 #gallons
            dishwasher = (45/60) * 1350 # watts
            dishwasherWaterHeater = (6 * 4)/60 * 4500 #watts
        else:
            dishwasherWater = 0 #gallons
            dishwasher = 0 # watts
            dishwasherWaterHeater = 0 #watts
        if date in laundryOnNov:
            washerWater = 15 #gallons
            washer = (30/60) * 500 #watts
            washerWaterHeater = (20 * .85 * 4)/60 * 4500 #watts
            dryer = (30/60) * 3000 #watts
        else:
            washerWater = 0 #gallons
            washer = 0 #watts
            washerWaterHeater = 0 #watts
            dryer = 0 #watts

        refridgerator = 150 * 24 #watts
        lightsUsageHours = 0
        # lights = ['bedroom1_light1', 'bedroom1_light2', 'bedroom1_light3', 'bedroom2_light1', 'bedroom2_light2', 'bedroom2_light3', 'bedroom3_light1', 'bedroom3_light2', 'bedroom3_light3', 'kitchen_light', 'living_room_light1', 'living_room_light2', 'living_room_light3']
        for i in range(random.randint(4, 16)):
            lightsUsageHours += random.uniform(0, 7)
        lights = lightsUsageHours * 60

        bathExhaust = sum([random.uniform(0, 1) for i in range(random.randint(3, 12))]) * 30

        HVACon = random.uniform(60, 180) #minutes
        hvac = (HVACon/60) * 3500

        totalPower = microwave + stove + oven + livingRoomTV + bedroomTV + showerWaterHeater + bathWaterHeater + dishwasher + washer + refridgerator + lights + bathExhaust + hvac + dishwasherWaterHeater + washerWaterHeater + dryer
        totalWater = showerWater + bathWater + dishwasherWater + washerWater

        totalPowerCost = round(totalPower/1000 * 0.13, 2)
        totalWaterCost = totalWater * 0.0252

        print(totalPower)
        print(totalWater)
        print(totalPowerCost)
        print(totalWaterCost)
        cur.execute(execute, (date, totalPower, totalWater, totalPowerCost, totalWaterCost, totalPowerCost + totalWaterCost))
    conn.commit()
    cur.close()
    conn.close()

def randomizeDecData(days, decBegin, dishwasherOnDec, laundryOnDec, dec):
    conn = getConnection()
    cur = getCursor(conn)
    execute = "INSERT INTO usageHistory (day, power, water, powerCost, waterCost, totalCost) VALUES (%s, %s, %s, %s, %s, %s)"
    for date in dec:
        day = days[(decBegin + int(date[-2:]) - 1) % 7]
        if day[0] == 'S':
            microwave = (30/60) * 1000 #watts
            stove = (30/60) * 3000 #watts
            oven = (60/60) * 1200 #watts
            livingRoomTV = 8 * 200 #watts
            bedroomTV = 4 * 200 #watts
            showerWater = 20 * 3 #gallons
            showerWaterHeater = (25 * .65 * 3 * 4)/60 * 4500 #watts
            bathWater = 36 * 3 #gallons
            bathWaterHeater = (30 * .65 * 3 * 4)/60 * 4500 #watts
        else: 
            microwave = (20/60) * 1000 #watts
            stove = (15/60) * 3000 #watts
            oven = (45/60) * 1200 #watts
            livingRoomTV = 4 * 200 #watts
            bedroomTV = 2 * 200 #watts
            showerWater = 20 * 2 #gallons
            showerWaterHeater = (25 * .65 * 2 * 4)/60 * 4500 #watts
            bathWater = 36 * 2 #gallons
            bathWaterHeater = (30 * .65 * 2 * 4)/60 * 4500 #watts
        if date in dishwasherOnDec:
            dishwasherWater = 7 #gallons
            dishwasher = (45/60) * 1350 # watts
            dishwasherWaterHeater = (6 * 4)/60 * 4500 #watts
        else:
            dishwasherWater = 0 #gallons
            dishwasher = 0 # watts
            dishwasherWaterHeater = 0 #watts
        if date in laundryOnDec:
            washerWater = 15 #gallons
            washer = (30/60) * 500 #watts
            washerWaterHeater = (20 * .85 * 4)/60 * 4500 #watts
            dryer = (30/60) * 3000 #watts
        else:
            washerWater = 0 #gallons
            washer = 0 #watts
            washerWaterHeater = 0 #watts
            dryer = 0 #watts

        refridgerator = 150 * 24 #watts
        lightsUsageHours = 0
        # lights = ['bedroom1_light1', 'bedroom1_light2', 'bedroom1_light3', 'bedroom2_light1', 'bedroom2_light2', 'bedroom2_light3', 'bedroom3_light1', 'bedroom3_light2', 'bedroom3_light3', 'kitchen_light', 'living_room_light1', 'living_room_light2', 'living_room_light3']
        for i in range(random.randint(4, 16)):
            lightsUsageHours += random.uniform(0, 7)
        lights = lightsUsageHours * 60

        bathExhaust = sum([random.uniform(0, 1) for i in range(random.randint(3, 12))]) * 30

        HVACon = random.uniform(60, 180) #minutes
        hvac = (HVACon/60) * 3500

        totalPower = microwave + stove + oven + livingRoomTV + bedroomTV + showerWaterHeater + bathWaterHeater + dishwasher + washer + refridgerator + lights + bathExhaust + hvac + dishwasherWaterHeater + washerWaterHeater + dryer
        totalWater = showerWater + bathWater + dishwasherWater + washerWater

        totalPowerCost = round(totalPower/1000 * 0.13, 2)
        totalWaterCost = totalWater * 0.0252

        print(totalPower)
        print(totalWater)
        print(totalPowerCost)
        print(totalWaterCost)
        cur.execute(execute, (date, totalPower, totalWater, totalPowerCost, totalWaterCost, totalPowerCost + totalWaterCost))
    conn.commit()
    cur.close()
    conn.close()

def randomizedData():
    #All watts in hours
    conn = getConnection()
    cur = getCursor(conn)
    # cur.execute('''CREATE TABLE usageHistory(day DATE, power NUMERIC, water NUMERIC, powerCost NUMERIC, waterCOST NUMERIC, totalCost NUMERIC)''')
    conn.commit()
    oct = [f'2020-10-{i}' if len(str(i)) == 2 else f'2020-10-0{i}' for i in range(1, 32)]
    nov = [f'2020-11-{i}' if len(str(i)) == 2 else f'2020-11-0{i}' for i in range(1, 31)]
    dec = [f'2020-12-{i}' if len(str(i)) == 2 else f'2020-12-0{i}' for i in range(3, 4)]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']
    octBegin = 3
    novBegin = 6
    decBegin = 1

    dishwasherOnOct = ['2020-10-01', '2020-10-03']
    laundryOnOct = ['2020-10-03']
    for i in range(3, len(oct), 7):
        daysOfWeekDish = oct[i:i+7]
        daysOfWeekLaundry = oct[i:i+7]
        for j in range(4):
            dishOnDay = random.choice(daysOfWeekDish)
            dishwasherOnOct.append(dishOnDay)
            daysOfWeekDish.remove(dishOnDay)

            laundryOnDay = random.choice(daysOfWeekLaundry)
            laundryOnOct.append(laundryOnDay)
            daysOfWeekLaundry.remove(laundryOnDay)


    dishwasherOnNov = ['2020-11-30']
    laundryOnNov = ['2020-11-29']
    for i in range(0, len(nov) - 2, 7):
        daysOfWeekDish = nov[i:i+7]
        daysOfWeekLaundry = nov[i:i+7]
        for j in range(4):
            dishOnDay = random.choice(daysOfWeekDish)
            dishwasherOnNov.append(dishOnDay)
            daysOfWeekDish.remove(dishOnDay)

            laundryOnDay = random.choice(daysOfWeekLaundry)
            laundryOnNov.append(laundryOnDay)
            daysOfWeekLaundry.remove(laundryOnDay)

    dishwasherOnDec = ['2020-12-01']
    laundryOnDec = ['2020-12-03']

    # randomizeOctoberData(days, octBegin, dishwasherOnOct, laundryOnOct, oct)
    # randomizeNovData(days, novBegin, dishwasherOnNov, laundryOnNov, nov)
    randomizeDecData(days, decBegin, dishwasherOnDec, laundryOnDec, dec)

    cur.close()
    conn.close()

def enterAppliances():
    conn = getConnection()
    cur = getCursor(conn)
    cur.execute('''CREATE TABLE appliances(name TEXT, status TEXT, startTime TIME, totalUsage NUMERIC, power INT, gallons INT [])''') #Gallons: [gallons, hot, cold]
    execute = "INSERT INTO appliances (name, status, startTime, totalUsage, power, gallons) VALUES (%s, %s, %s, %s, %s, %s)"

    #Light bulbs
    cur.execute(execute,('bedroom1_light1', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom1_light2', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom1_light3', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom2_light1', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom2_light2', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom2_light3', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom3_light1', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom3_light2', 'off', None, None, 60, None))
    cur.execute(execute,('bedroom3_light3', 'off', None, None, 60, None))
    cur.execute(execute,('bathroom1_light', 'off', None, None, 60, None))
    cur.execute(execute,('bathroom2_light', 'off', None, None, 60, None))
    cur.execute(execute,('kitchen_light', 'off', None, None, 60, None))
    cur.execute(execute,('living_room_light1', 'off', None, None, 60, None))
    cur.execute(execute,('living_room_light2', 'off', None, None, 60, None))
    cur.execute(execute,('living_room_light3', 'off', None, None, 60, None))

    #Doors and windows
    cur.execute(execute,('living_room_door1', 'closed', None, None, None, None))
    cur.execute(execute,('living_room_door2', 'closed', None, None, None, None))
    cur.execute(execute,('kitchen_door1', 'closed', None, None, None, None))
    cur.execute(execute,('window', 'closed', None, None, None, None))

    #other
    cur.execute(execute,('bath_exhaust_fan', 'off', None, None, 30, None))
    cur.execute(execute,('HVAC', 'off', None, None, 3500, None))
    cur.execute(execute,('refridgerator', 'on', None, None, 150, None))
    cur.execute(execute,('microwave', 'off', None, None, 1000, None))
    cur.execute(execute,('water_heater', 'off', None, None, 4500, None))
    cur.execute(execute,('stove', 'off', None, None, 3000, None))
    cur.execute(execute,('oven', 'off', None, None, 1200, None))
    cur.execute(execute,('living_room_tv', 'off', None, None, 200, None))
    cur.execute(execute,('bedroom_tv', 'off', None, None, 200, None))
    cur.execute(execute,('dishwasher', 'off', None, None, 1350, [7, 100, 0])) 
    cur.execute(execute,('washer', 'off', None, None, 500, [15, 85, 15]))
    cur.execute(execute,('dryer', 'off', None, None, 3000, None))
    cur.execute(execute,('bath', 'off', None, None, None, [36, 65, 35]))
    cur.execute(execute,('shower', 'off', None, None, None, [20, 65, 35]))
    cur.execute(execute, ('video_game_console', 'off', None, None, 150, None))
    cur.execute(execute, ('cable_box', 'off', None, None, 35, None))


    conn.commit()
    cur.close()
    conn.close()

def enterHome():
    conn = getConnection()
    cur = getCursor(conn)
    cur.execute('''CREATE TABLE home(name TEXT, appliances TEXT [], internalTemp NUMERIC, totalPower NUMERIC, totalWater NUMERIC, totalUsage NUMERIC)''') 
    execute = "INSERT INTO home (name, appliances, internalTemp, totalPower, totalWater, totalUsage) VALUES (%s, %s, %s, %s, %s, %s)"
    appliances = ['bedroom1_light1', 'bedroom1_light2', 'bedroom1_light3', 'bedroom2_light1', 'bedroom2_light2', 'bedroom2_light3', 'bedroom3_light1', 'bedroom3_light2', 'bedroom3_light3', 'kitchen_light', 'living_room_light1', 'living_room_light2', 'living_room_light3', 'living_room_door1', 'living_room_door2', 'kitchen_door1', 'window', 'bath_exhaust_fan', 'HVAC', 'refriderator', 'microwave', 'water_heater', 'stove', 'oven', 'living_room_tv', 'bedroom_tv', 'dishwasher', 'washer', 'dryer', 'bath', 'shower']
    cur.execute(execute, ('smartHome1', appliances, 72, 0, 0, 0, 0))
    conn.commit()
    cur.close()
    conn.close()

randomizedData()

conn = getConnection()
cur = getCursor(conn)
cur.execute('SELECT * FROM usageHistory')
data = (cur.fetchall())
for d in data: 
    print(d)
cur.close()
conn.close()