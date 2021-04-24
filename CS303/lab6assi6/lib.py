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
    b = ins_sort(arr)
    for i in b:
        arr[b.index(i)] = i

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

def merge_sort_w(A):
    return merge_sort(A, A[:], 0, len(A) - 1)

"""
An array class to make the pseudocode easier to implement.
"""
class Array:
    def __init__(self, arr):
        self.arr = arr
        self.heap_size = len(arr) - 1

def max_heapify(A, i):
    l = 2*i + 1
    r = 2*i + 2
    if l <= A.heap_size and A.arr[l] > A.arr[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A.arr[r] > A.arr[largest]:
        largest = r
    if largest != i:
        A.arr[i], A.arr[largest] = A.arr[largest], A.arr[i]
        max_heapify(A, largest)    

def build_max_heap(A):
    i = len(A.arr)//2
    while i >= 0:
        max_heapify(A, i)
        i -= 1

def heap_sort(A):
    Arr = Array(A)
    build_max_heap(Arr)
    #https://realpython.com/python-range/#decrementing-with-range
    for i in range(len(Arr.arr) - 1, 0, -1):
        #https://stackoverflow.com/a/2493962/9295513
        Arr.arr[0], Arr.arr[i] = Arr.arr[i], Arr.arr[0]
        Arr.heap_size -= 1
        max_heapify(Arr, 0)