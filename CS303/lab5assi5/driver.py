from time import perf_counter as perf
from quick_sort import quicksort, med_quicksort
from lib import ins_sort_wrapper, merge_sort_w, heap_sort

files = ['input_16.txt', 'input_32.txt', 'input_64.txt', 'input_128.txt', 'input_256.txt', 'input_512.txt', 'input_1024.txt', 'input_2048.txt', 'input_4096.txt', 'input_8192.txt']

more_files = ['Input_Random.txt', 'Input_ReversedSorted.txt', 'Input_Sorted.txt']

all_files = files + more_files

for file in all_files:
    inputFile = open(file, "r")
    inputs = inputFile.read()
    inputs = inputs.lstrip()
    inputs = inputs.split()
    inputFile.close()

    print("\n\t" + file + "\n")
    sort1 = [int(i) for i in inputs if i != ' ']
    sort2 = [int(i) for i in inputs if i != ' ']
    sort3 = [int(i) for i in inputs if i != ' ']
    sort4 = [int(i) for i in inputs if i != ' ']
    sort5 = [int(i) for i in inputs if i != ' ']
    start = perf()
    ins_sort_wrapper(sort1)
    total = perf() - start
    print("Insertion sort time:\t\t{}".format(total))
    start = perf()
    merge_sort_w(sort2)
    total = perf() - start
    print("Merge sort time:\t\t{}".format(total))
    start = perf()
    heap_sort(sort3)
    total = perf() - start
    print("Heap sort time:\t\t{}".format(total))
    start = perf()
    quicksort(sort4)
    total = perf() - start
    print("Quick sort time:\t\t{}".format(total))
    start = perf()
    med_quicksort(sort5)
    total = perf() - start
    print("Quick sort with median time:\t\t{}".format(total))
    