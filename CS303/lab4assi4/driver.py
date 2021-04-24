from heap_sort import *
from time import perf_counter as perf

files = ['input_100.txt', 'input_1000.txt', 'input_5000.txt', 'input_10000.txt', 'input_50000.txt', 'input_100000.txt', 'input_500000.txt']

for file in files:
   inputFile = open(file, "r")
   inputs = inputFile.read()
   inputs = inputs.lstrip()
   inputs = inputs.split()
   inputFile.close()
   #https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
   sort1 = [int(i) for i in inputs if i != ' ']
   sort2 = [int(i) for i in inputs if i != ' ']
   sort3 = [int(i) for i in inputs if i != ' ']
   #Test Heap
   start = perf()
   heap_sort(sort1)
   end = perf()
   print("Heap:", str(end - start))
   #Test Merge
   start = perf()
   tim_sort(sort2, sort2[:], 0, len(sort2) - 1, 4096)
   end = perf()
   print("Merge:", str(end - start))
   #Test Insertion
   start = perf()
   heap_sort(sort3)
   end = perf()
   print("Insertion:", str(end - start))