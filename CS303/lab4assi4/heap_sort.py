from random import randrange

#Skip to line 61, the following is just for the driver

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

def main():
    #Test on a fixed-size array.
    a = [198, 389, 216, 21, 23, 24, 17, 200]
    b = a[:]
    a.sort()
    print("Standard Library Sort: " + str(a))
    heap_sort(b)
    print("Heap Sort: {}\nDid it work? {}".format(b, a == b))
    #The following tests random elements
    errors = 0
    print("Does it work for many elements? Hold on a sec'...")
    for k in range(500):
        a = [randrange(1, 400) for i in range(400)]
        b = a[:]
        a.sort()
        heap_sort(b)
        if b != a:
            print("trouble")
            print(a)
            print(b)
            errors += 1
    print(errors == 0)
    #Test on zero elements
    emptyArr = []
    e = emptyArr[:]
    e.sort()
    heap_sort(emptyArr)
    print("Empty Array: {}".format(emptyArr == e))
    #Test on reverse sorting
    revSorted = [5, 4, 3, 2, 1]
    r = revSorted[:]
    r.sort()
    heap_sort(revSorted)
    print("Reverse Sorted: {}".format(revSorted == r))
    #Test on one element
    oneElem = [1]
    o = oneElem[:]
    o.sort()
    heap_sort(oneElem)
    print("One Element: {}".format(oneElem == o))

if __name__ == "__main__":
    main()