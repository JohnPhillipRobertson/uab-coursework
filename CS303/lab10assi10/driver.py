from RBT import *
from HashMap import *
from time import perf_counter as p

import sys
sys.setrecursionlimit(2**31 - 1)

tupni = open("input.dat", "r")
inputs = []
line = tupni.readline()
while line != '':
    inputs.append(line.split(","))
    line = tupni.readline()
tupni.close()
keys = []
for i in inputs:
    keys.append(int(i[0]))

CPU = open("UPC-random.csv", "r")
inputs = []
ruby = RBT()
line = CPU.readline()
while line != '':
    inputs.append(line.split(","))
    line = CPU.readline()
CPU.close()

q = p()
for i in inputs:
    ruby.RBinsert(*(int(i[0]), i[1] + i[2]))
print("Time taken to insert: {}".format(p() - q))

print("Testing by hand: ")
print("79: {}".format(ruby.tree_search(79)))
print("161: {}".format(ruby.tree_search(161)))
print("100000000 (fake value): {}\n".format(ruby.tree_search(100000000)))


print("Speed test using keys from input.dat")
q = p()
for i in keys:
    print(ruby.tree_search(i))
print("Time taken to extract: {}".format(p() - q))
print("Note that this changes by an order of magnitude\nif you print the ouputs")

print("\nLet's compare that all to HashMap:")
q = p()
linMap = HashMap(20000000)
for i in inputs:
    linMap.put(*(int(i[0]), i[1] + i[2]), "lin")
print("Time for linear insertion: {}".format(p() - q))
q = p()
for i in keys:
    print(linMap.get(i))
print("Time for linear extraction: {}".format(p() - q))
del linMap

print()
q = p()
quadMap = HashMap(20000000)
for i in inputs:
    quadMap.put(*(int(i[0]), i[1] + i[2]), "quad")
print("Time for quadratic insertion: {}".format(p() - q))
q = p()
for i in keys:
    print(quadMap.get(i, "quad"))
print("Time for quadratic extraction: {}".format(p() - q))
del quadMap

print()
q = p()
custMap = HashMap(20000000)
for i in inputs:
    custMap.put(*(int(i[0]), i[1] + i[2]), "quad")
print("Time for the given function's insertion: {}".format(p() - q))
q = p()
for i in keys:
    print(custMap.get(i, "cust"))
print("Time for given function extraction: {}".format(p() - q))
del custMap
