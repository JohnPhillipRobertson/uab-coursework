import requests,json,re

web = "https://vpic.nhtsa.dot.gov/api"

#Decode VIN
def decodeVin(vin,year):
    url = web +"/vehicles/DecodeVinExtended/"+vin+"?format=json&modelyear="+year+""
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Decode WMI
def decodeWMI(wmiID):
    url = web + "/vehicles/decodewmi/"+wmiID+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest


#Get WMIs for Manufacturer
def getWMIsM(make):
    url = web + "/vehicles/GetWMIsForManufacturer/"+make+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get All Makes
def getAllMakes():
    url = web + "/vehicles/GetAllMakes?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Manufacturer Details
def getMan(make):
    url = web + "/vehicles/GetManufacturerDetails/"+make+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Makes for Manufacturer by Manufacturer Name and Year (Available if needed)
def getMfMbMNaY(Mft, year):
    url = web + "/vehicles/GetMakesForManufacturerAndYear/"+make+"?year="+year+"&format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Makes for Vehicle Type by Vehicle Type Name
def getMVType(type):
    url = web + "/vehicles/GetMakesForVehicleType/"+type+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Vehicle Types for Make by Name
def getTypeMake(make):
    url = web + "/vehicles/GetVehicleTypesForMake/"+make+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Vehicle Types for Make by Id
def getTypeMakeID(id):
    url = web + "/vehicles/GetVehicleTypesForMakeId/"+id+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Models for Make
def getAllModels(make):
    url = web + "/vehicles/GetModelsForMake/"+make+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Models for MakeId
def getAllModelsMI(makeID):
    url = web + "/vehicles/GetModelsForMakeId/"+makeID+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Models for Make and a combination of Year and Vehicle Type
def modelsbyMakeYear(make, year):
    url = web + "/vehicles/GetModelsForMakeYear/make/"+make+"/modelyear/"+year+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest
def modelsbyMakeType(make, type):
    url = web + "/vehicles/GetModelsForMakeYear/make/"+make+"/vehicletype/"+type+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest
def modelsbyMakeTypeYear(make,year,type):
    url = web + "/vehicles/GetModelsForMakeYear/make/"+make+"/modelyear/"+year+"/vehicletype/"+type+"?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Vehicle Variables List
def getVVL():
    url = web + "/vehicles/getvehiclevariablelist?format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#Get Equipment Plant Codes (Available if needed year > 2016, typeNum = 1-4, report = [new, updated, closed, all])
def getEquipPlantCodes(year,typeNum,report):
    url = web +"/vehicles/GetEquipmentPlantCodes?year="+year+"&equipmentType="+typeNum+"&reportType="+report+"&format=json"
    r = requests.get(url).text
    dic = json.loads(r)
    myRequest = dic["Results"]
    return myRequest

#API Helper function
def getResults(r,t):
    list = []
    for i in r:
        list.append(i[t])
    return list

#Obtain URLs
def get_urls(urls, reg_ex):

    url_list = []

    for relev in urls:
        r = requests.get(relev, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}).text  # This header had to be taken from elsewhere because some ID needs to be given, and I don't know how to give my own.
        regex = re.compile(reg_ex, re.M)
        url_list += regex.findall(r)

    url_list = ["https://www.discounttire.com" + i for i in url_list]

    return url_list

#Decode URLs
def name_url(s, w):
    if not w:
        s = s[39:len(s)-1]
    else:
        s = s[40:len(s)-1]
    s = s.split("-")
    s = [i.title() for i in s]
    s = " ".join(s)
    return s

tire_urls = [
    "https://www.discounttire.com/tires/all-season-catalog",
    "https://www.discounttire.com/tires/all-terrain-catalog",
    "https://www.discounttire.com/tires/atv-utv-catalog",
    "https://www.discounttire.com/tires/competition-catalog",
    "https://www.discounttire.com/tires/lawn-catalog",
    "https://www.discounttire.com/tires/mud-terrain-catalog",
    "https://www.discounttire.com/tires/passenger-catalog",
    "https://www.discounttire.com/tires/performance-catalog",
    "https://www.discounttire.com/tires/spare-catalog",
    "https://www.discounttire.com/tires/summer-catalog",
    "https://www.discounttire.com/tires/touring-catalog",
    "https://www.discounttire.com/tires/trailer-catalog",
    "https://www.discounttire.com/tires/truck-catalog",
    "https://www.discounttire.com/tires/winter-catalog"
]

wheel_urls = [
    "https://www.discounttire.com/wheels/atv-utv-catalog",
    "https://www.discounttire.com/wheels/chrome-catalog",
    "https://www.discounttire.com/wheels/machined-catalog",
    "https://www.discounttire.com/wheels/mesh-catalog",
    "https://www.discounttire.com/wheels/modular-catalog",
    "https://www.discounttire.com/wheels/multi-spoke-catalog",
    "https://www.discounttire.com/wheels/painted-catalog",
    "https://www.discounttire.com/wheels/passenger-catalog",
    "https://www.discounttire.com/wheels/split-spoke-catalog",
    "https://www.discounttire.com/wheels/split-spoke-catalog",
    "https://www.discounttire.com/wheels/truck-catalog"
]
