from HashMap import *
from time import perf_counter

tupni = open("input.dat", "r")
inputs = []
line = tupni.readline()
while line != '':
    inputs.append(line.split(","))
    line = tupni.readline()
tupni.close()
keys = []
types = ["lin", "quad", "cust"]
for tipe in types:
    start = perf_counter()
    for i in inputs:
        mesa = HashMap()
        j = (int(i[0]), i[1] + i[2])
        keys.append(int(i[0]))
        mesa.put(*j, probe_type=tipe)
    for i in keys:
        print(mesa.get(i, tipe))
    print("{}-insert performance: {}".format(tipe, perf_counter() - start))
    del mesa

LINES = 177650


def test(mode):
    CPU = open("UPC-random.csv", "r")
    inputs = []
    line = CPU.readline()
    while line != '':
        inputs.append(line.split(","))
        line = CPU.readline()
    CPU.close()
    mesa = HashMap(LINES*2)
    start = perf_counter()
    for i in inputs:
        j = (int(i[0]), i[1] + i[2])
        mesa.put(*j, mode)
    print("\nThat took {} seconds.".format(perf_counter() - start))

    print("\tThree manual searches to test if this works:")
    target = mesa.get(79)
    print(target)
    target = mesa.get(93)
    print(target)
    target = mesa.get(2160500567)
    print(target)
    print("\tNow to do this iteratively:")
    for i in keys:
        start = perf_counter()
        target = mesa.get(int(i))
        print(target)
        print("\t{} seconds.".format(perf_counter() - start))


test("lin")
print("-"*80)
test("quad")
