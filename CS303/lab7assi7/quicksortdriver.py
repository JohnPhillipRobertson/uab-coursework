from time import perf_counter as p
files = ['input_100.txt', 'input_1000.txt', 'input_5000.txt',
         'input_10000.txt', 'input_50000.txt', 'Input_Sorted.txt', 'Input_ReversedSorted.txt', 'Input_Random.txt']
for fi in files:
    inputFile = open(fi, "r")
    inputs = inputFile.read()
    inputs = inputs.lstrip()
    inputs = inputs.split()
    inputFile.close()
    sortable = [int(i) for i in inputs if i != ' ']
    from reverseLib import rev_quicksort
    # Quick sort
    print("Quick", end=", ")
    q = p()
    rev_quicksort(sortable)
    print(p() - q)
