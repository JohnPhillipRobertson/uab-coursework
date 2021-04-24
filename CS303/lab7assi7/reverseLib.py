from random import randrange
from sys import setrecursionlimit
setrecursionlimit(2**31 - 1)


def ins_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return A


def merge(A, temp, p, q, r):
    # merge A[p..q] with A[q+1..r]
    i = p
    j = q + 1
    # copy A[p..r] to temp[p..r]
    for k in range(p, r + 1):
        temp[k] = A[k]
    for k in range(p, r + 1):
        if i > q:
            A[k] = temp[j]
            j += 1
        elif j > r:
            A[k] = temp[i]
            i += 1
        elif temp[j] > temp[i]:
            A[k] = temp[j]
            j += 1
        else:
            A[k] = temp[i]
            i += 1


def merge_sort(A, temp, p, r):
    if p < r:
        q = (p + r)//2
        merge_sort(A, temp, p, q)
        merge_sort(A, temp, q + 1, r)
        merge(A, temp, p, q, r)


def rev_merge_sort(A):
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
    if l <= A.heap_size and A.arr[l] < A.arr[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A.arr[r] < A.arr[largest]:
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
    for i in range(len(Arr.arr) - 1, 0, -1):
        Arr.arr[0], Arr.arr[i] = Arr.arr[i], Arr.arr[0]
        Arr.heap_size -= 1
        max_heapify(Arr, 0)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def rev_quicksort(A):
    def _quicksort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            _quicksort(A, p, q - 1)
            _quicksort(A, q + 1, r)
    _quicksort(A, 0, len(A) - 1)


def rev_bubble_sort(A):
    for i in range(len(A) - 1):
        j = len(A) - 1
        while j >= i + 1:
            if A[j] > A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]
            j -= 1


def rev_selection_sort(A):
    for i in range(len(A) - 1):
        min = i
        j = i + 1
        while j < len(A):
            if A[j] > A[min]:
                min = j
            j += 1
        if i != min:
            A[min], A[i] = A[i], A[min]