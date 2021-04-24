from random import randrange, randint
from time import perf_counter as perf

def ins_sort(arr):
    A = arr[:]
    for j in range(len(A)):
        #skip over first elem
        if j < 1:
            continue
        #end skip
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A

def ins_sort_wrapper(arr):
    arr = ins_sort(arr)

def merge(A, temp, p, q, r):
    #merge A[p..q] with A[q+1..r]
    i = p
    j = q + 1
    #copy A[p..r] to temp[p..r]
    for k in range(p, r+1):
        temp[k] = A[k]
    #merge back to A[p..r]
    for k in range(p, r+1):
        if i > q: #left half empty, copy from the right
            A[k] = temp[j]
            j += 1
        elif j > r: #right half empty, copy from the left
            A[k] = temp[i]
            i += 1
        elif temp[j] < temp[i]: #copy from the right
            A[k] = temp[j]
            j += 1
        else:
            A[k] = temp[i] #copy from the left
            i += 1

def merge_sort(A, temp, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(A, temp, p, q)
        merge_sort(A, temp, q + 1, r)
        merge(A, temp, p, q, r)

def tim_sort(A, temp, p, r, thresh):
    if len(A) <= thresh:
        ins_sort_wrapper(A)
    elif p < r:
        q = (p + r)//2
        merge_sort(A, temp, p, q)
        merge_sort(A, temp, q + 1, r)
        merge(A, temp, p, q, r)

# #Test on a fixed-size array.
# a = [198, 389, 216, 21, 23, 24, 17, 200]
# b = a[:]
# a.sort()
# tim_sort(b, b[:], 0, len(b)-1, 4)
# print(a)
# print(b)
# print(a == b)
# #The following tests random elements
# errors = 0
# for k in range(1000):
    # a = [randrange(1, 400) for i in range(400)]
    # b = a[:]
    # a.sort()
    # tim_sort(b, b[:], 0, len(b)-1)
    # if b != a:
        # print("trouble")
        # print(a)
        # print(b)
        # errors += 1
# if errors == 0:
    # print("True")
# #Test on zero elements
# emptyArr = []
# e = emptyArr[:]
# e.sort()
# tim_sort(emptyArr, emptyArr[:], 0, len(emptyArr)-1, 4)
# print(emptyArr == e)
# #Test on reverse sorting
# revSorted = [5, 4, 3, 2, 1]
# r = revSorted[:]
# r.sort()
# tim_sort(revSorted, revSorted[:], 0, len(revSorted)-1, 4)
# print(revSorted == r)
# #Test on one element
# oneElem = [1]
# o = oneElem[:]
# o.sort()
# tim_sort(oneElem, oneElem[:], 0, len(oneElem)-1, 4)
# print(oneElem == o)

files = ['input_100.txt', 'input_1000.txt', 'input_5000.txt', 'input_10000.txt', 'input_50000.txt', 'input_100000.txt', 'input_500000.txt']

for i in range(5):
    print("Insertion Threshold of {}:".format(2048*i))
    for file in files:
       inputFile = open(file, "r")
       inputs = inputFile.read()
       inputs = inputs.lstrip()
       inputs = inputs.split()
       inputFile.close()
       #https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats
       this_must_be_sorted = [int(i) for i in inputs if i != ' ']
       start = perf()
       tim_sort(this_must_be_sorted, this_must_be_sorted[:], 0, len(this_must_be_sorted)-1, 2048*i)
       end = perf()
       print(str(end - start), end="|")
    print("")