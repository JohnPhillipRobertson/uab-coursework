from reverseLib import *
from time import perf_counter as p
from random import randrange

for i in (ins_sort, rev_merge_sort, heap_sort, rev_quicksort, rev_bubble_sort, rev_selection_sort):
    print(i, end=", ")
    a = [randrange(512) for x in range(512)]
    b = a[:]
    i(a)
    b.sort(reverse=True)
    print(a == b)

files = ['Input_Random.txt', 'Input_ReversedSorted.txt', 'Input_Sorted.txt',
         'input_100.txt', 'input_1000.txt', 'input_5000.txt', 'input_10000.txt', 'input_50000.txt']

for file in files:
    print(file)
    inputFile = open(file, "r")
    inputs = inputFile.read()
    inputs = inputs.lstrip()
    inputs = inputs.split()
    inputFile.close()
    sortable = [int(i) for i in inputs if i != ' ']
    # Insertion sort
    print("Insertion", end=", ")
    q = p()
    ins_sort(sortable)
    print(p() - q)
    # Merge sort
    print("Merge", end=", ")
    q = p()
    rev_merge_sort(sortable)
    print(p() - q)
    # Heap sort
    print("Heap", end=", ")
    q = p()
    heap_sort(sortable)
    print(p() - q)
    # Bubble sort
    print("Bubble", end=", ")
    q = p()
    rev_bubble_sort(sortable)
    print(p() - q)
    # Selection sort
    print("Selection", end=", ")
    q = p()
    rev_selection_sort(sortable)
    print(p() - q)
