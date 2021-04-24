from insSort import ins_sort
from time import perf_counter as perf
from random import randrange

files = ['input_100.txt', 'input_1000.txt', 'input_5000.txt', 'input_10000.txt', 'input_50000.txt', 'input_100000.txt', 'input_500000.txt']

for file in files:
    inputFile = open(file, "r")
    inputs = inputFile.read()
    inputs = inputs.lstrip()
    inputs = inputs.split()
    inputFile.close()
    #https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
    this_must_be_sorted = [int(i) for i in inputs if i != ' ']
    start = perf()
    ins_sort(this_must_be_sorted)
    end = perf()
    print(str(end - start))
