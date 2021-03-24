from meteostat import Hourly, Stations
from datetime import *

def getTemp(date):
    date = [int(num) for num in date.split('-')]
    dateBegin = datetime(date[0], date[1], date[2])
    dateEnd = datetime(date[0], date[1], date[2], 23, 59)
    stations = Stations(lat = 33.5624, lon = -86.7541)
    station = stations.fetch(1)

    hourly_data = Hourly(station, start = dateBegin, end = dateEnd)
    hourly_data = hourly_data.normalize().interpolate(limit = 6).fetch()
    return list(hourly_data['temp'])
