from random import randrange, randint
from lib import ins_sort_wrapper
from time import perf_counter as perf
from novelsort import novel_sort, transaction_sort

def novel_sort_tester(oneMany):
    def randolist(x):
        for i in range(256):
            x.append(randint(16, 256))
    counter = 0
    for i in range(oneMany):
        l = []
        randolist(l)
        x = l[:]
        novel_sort(l)
        x.sort()
        if x == l:
            counter += 1
    print("The test executed {} times, and it ".format(oneMany), end="")
    if counter == oneMany:
        print("got it right every time.")
    else:
        print("messed up somewhere along the way.")

loganaysegul = input("Enter '1' to test the novel sorting algorithm once\nor press any key to test it a random but arbitrarily large amount of times")
if loganaysegul == '1':
    novel_sort_tester(1)
else:
    novel_sort_tester(randint(128, 1024))
print("There's a few other tests too:")
empty = []
novel_sort(empty)
print("Empty array:", str(empty))
rev = [10, 9, 8, 7, 6, 5, 4, 3, 2, -1000]
novel_sort(rev)
print("Reverse sorted array:", str(rev))    

files1 = ['input_16.txt', 'input_32.txt', 'input_64.txt', 'input_128.txt', 'input_256.txt', 'input_512.txt', 'input_1024.txt', 'input_2048.txt', 'input_4096.txt', 'input_8192.txt', 'Input_Sorted.txt']

def optional():
    for file in files1:
        inputFile = open(file, "r")
        inputs = inputFile.read()
        inputs = inputs.lstrip()
        inputs = inputs.split()
        inputFile.close()
        this_must_be_sorted = [int(i) for i in inputs if i != ' ']
        start = perf()
        novel_sort(this_must_be_sorted)
        end = perf()
        print(str(end - start))
    print("Let's try that with insertion sort to compare")
    for file in files1:
        inputFile = open(file, "r")
        inputs = inputFile.read()
        inputs = inputs.lstrip()
        inputs = inputs.split()
        inputFile.close()
        this_must_be_sorted = [int(i) for i in inputs if i != ' ']
        start = perf()
        ins_sort_wrapper(this_must_be_sorted)
        end = perf()
        print(str(end - start))
yes = input("If you would like to test the novel sorting function on the big files, press '1', else press any key.")
if yes:
    print("Here goes nothing")
    optional()


#Sorting the transactions
print()
files2 = ["NovelSortInput.txt", "myNovelSortInput1.txt"]
for file in files2:
    inputFile = open(file, "r")
    inputs = inputFile.read()
    inputs = inputs.split("\n")
    inputFile.close()
    for i in inputs:
        if i == "" or i == "\n":
            inputs.remove(i)
    transaction_sort(inputs)
    for i in inputs:
        print(i)
    print()