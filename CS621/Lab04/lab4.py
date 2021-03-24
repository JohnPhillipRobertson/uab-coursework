import COVID19Py
import json
# Part 1:
"""
Use the last example to get the live case numbers for United States of America. Display the
information of the state’s which has the most confirmed cases and least confirmed cases.
Additionally, display the average number of active cases.
"""
# https://stackoverflow.com/a/4760517/9295513
import subprocess
result = json.loads(subprocess.run(
    ["curl", "--location", "--request", "GET", "https://api.covid19api.com/live/country/united-states/status/confirmed"], stdout=subprocess.PIPE).stdout)
states = {}
avg_active = 0
for i in result:
    state = i["Province"]
    if state not in states.keys():
        states[state] = int(i["Confirmed"])
    else:
        states[state] += int(i["Confirmed"])
        avg_active += i["Active"]
# https://stackoverflow.com/a/3282904/9295513
most_confirmed = max(states, key=states.get)
least_confirmed = min(states, key=states.get)
avg_active = int(avg_active/len(states.keys()))

print("Most confirmed: {}\nLeast confirmed: {}\nAverage active cases:{}".format(
    most_confirmed, least_confirmed, avg_active))

# Part 2:

"""
Display a table which shows the total number of cases for each state in US.
"""

covid19 = COVID19Py.COVID19(data_source="csbs")
america = covid19.getLocationByCountryCode("US")
tableft = {}
for i in america:
    state = i["province"]
    if state not in tableft.keys():
        l = i["latest"]
        tableft[state] = int(l["confirmed"]) + \
            int(l["deaths"]) + int(l["recovered"])
    else:
        tableft[state] += int(l["confirmed"]) + \
            int(l["deaths"]) + int(l["recovered"])

print("Confirmed + Deaths + Recoveries per American province:")
print("_"*50)
print("State\t\t\tTotal Number of cases")
for i, j in tableft.items():
    print(str(i) + "\t\t\t" + str(j))
