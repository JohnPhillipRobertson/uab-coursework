from searchLib import *
from time import perf_counter as perf
from random import randrange, choice
from sys import setrecursionlimit

setrecursionlimit(20000)

#getting the random target

target = randrange(1000)

try:
    inputFile = open(r"C:\Users\Robertson\Desktop\cs303\lab1assi1\input_1000.txt", "r") #https://stackoverflow.com/questions/12201928/python-open-gives-ioerror-errno-2-no-such-file-or-directory
    inputs = inputFile.read()
    inputs.lstrip()
    inputs.split() #https://stackoverflow.com/questions/6429638/how-to-split-a-string-of-space-separated-numbers-into-integers
    inputFile.close()
    while True: #https://stackoverflow.com/questions/4606919/in-python-try-until-no-error
        try:
            target = int(choice(inputs)) #https://stackoverflow.com/questions/8420143/valueerror-could-not-convert-string-to-float-id
            break
        except ValueError:
            continue
except:
    print("ATTENTION: I hardcoded the file link. Since I shouldn't upload a zip, a relative filepath doesn't matter anyway.")

#end getting random target

print("Target: " + str(target))

for i in range(4, 25):
    arr = [randrange(i**2) for x in range(i**2)]
    arr.sort() #sort it here so it won't affect time checking measurement
    Lstart = perf()
    lin_search(arr, target)
    lin_search_time = perf() - Lstart
    print("Linear search time:" + str(lin_search_time))
    Bstart = perf()
    bin_search(arr, target)
    bin_search_time = perf() - Bstart
    print("Binary search time:" + str(bin_search_time))
    print("Binary search is faster: " + str(bin_search_time < lin_search_time))
    
    """
    x = -1
    b = bin_search(arr, target)
    try:
        x = arr.index(target)
    except ValueError:
        continue
    if b != x:
        print("fail: x = " + str(x) + " b = " + str(b))
    else:
        print("exit code 0: " + str(x))

    x = -1
    l = lin_search(arr, target)
    try:
        x = arr.index(target)
    except ValueError:
        continue
    if l != x:
        print("fail: x = " + str(x) + " l = " + str(b))
    else:
        print("exit code 0: " + str(x))
    """