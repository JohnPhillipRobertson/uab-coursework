from bst import *
from random import shuffle
from time import perf_counter

tupni = open("input.dat", "r")
inputs = []
line = tupni.readline()
while line != '':
    inputs.append(line.split(","))
    line = tupni.readline()
tupni.close()
tree = Tree()
keys = []
for i in inputs:
    j = (int(i[0]), i[1] + i[2])
    keys.append(i[0])
    tree.tree_insert(*j)
tree.inorder_tree_walk()

# Now we test performance.
CPU = open("UPC.csv", "r")
inputs = []
line = CPU.readline()
while line != '':
    inputs.append(line.split(","))
    line = CPU.readline()
CPU.close()
tree = Tree()
# On the unsorted data
shuffle(inputs)
start = perf_counter()
for i in inputs:
    j = (int(i[0]), i[1] + i[2])
    tree.tree_insert(*j)
print("\nThat took {} seconds.".format(perf_counter() - start))

#Can it search though?
print("\tThree manual searches to test if this works:")
target = tree.tree_search(79)
print(target.val)
target = tree.tree_search(93)
print(target.val)
target = tree.tree_search(2160500567)
print(target.val)
print("\tNow to do this iteratively:")
for i in keys:
    start = perf_counter()
    target = tree.tree_search(int(i))
    print(target.key, end=", ")
    print(target.val, end="")
    print("\t{} seconds.".format(perf_counter() - start))

# On the sorted data
bad_idea = input("Press '1' if you want to build a BST on the sorted inputs (please don't do this).")
if bad_idea == "1":
    del tree
    tree = Tree()
    inputs.sort()
    start = perf_counter()
    for i in inputs:
        j = (int(i[0]), i[1] + i[2])
        keys.append(i[0])
        tree.tree_insert(*j)
    print("That took {} seconds".format(perf_counter() - start))
