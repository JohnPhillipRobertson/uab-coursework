import sys
sys.setrecursionlimit(2**31 - 1)

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A):
    def _quicksort(A, p, r):
        if p < r:
            q = partition(A, p, r)
            _quicksort(A, p, q - 1)
            _quicksort(A, q + 1, r)
    _quicksort(A, 0, len(A) - 1)

def med_quicksort(A):
    def median3(A, i, j, k):
        return A.index(max([A[i], A[j], A[k]]))
    def _mqs(A, p, r):
        if p < r:
            N = r - p + 1
            m = median3(A, p, p + N//2, r)
            A[m], A[r] = A[r], A[m]
            q = partition(A, p, r)
            _mqs(A, p , q - 1)
            _mqs(A, q + 1, r)
    _mqs(A, 0, len(A) - 1)

if __name__ == "__main__":
    passed = 0
    l = [3, 272, 28, 1, 4, 5]
    r = l[:]
    u = l[:]
    print(l)
    l.sort()
    quicksort(r)
    med_quicksort(u)
    print(l, r, u)
    if l == r and r == u:
        passed += 1
    #random elements and library sort
    from random import randrange
    sortie = [randrange(16) for i in range(8)]
    sorted = sortie[:]
    sartorial = sortie[:]
    sortie.sort()
    med_quicksort(sorted)
    quicksort(sartorial)
    if sortie == sorted and sortie == sartorial:
        print("Simple test passed")
        passed += 1
    #More random elements
    sortie = [randrange(1024) for i in range(512)]
    sorted = sortie[:]
    sartorial = sortie[:]
    sortie.sort()
    med_quicksort(sorted)
    quicksort(sartorial)
    if sortie == sorted and sortie == sartorial:
        print("Big test passed")
        passed += 1
    #No elements
    empty = []
    try:
        med_quicksort(empty)
        quicksort(empty)
        print("Empty test passed")
        passed += 1
    except:
        print("Looks like that didn't work.")
    #Already sorted
    sortie = [i for i in range(512)]
    sorted = sortie[:]
    sartorial = sortie[:]
    sortie.sort()
    med_quicksort(sorted)
    quicksort(sartorial)
    if sortie == sorted and sortie == sartorial:
        print("Already sorted test passed")
        passed += 1
    #There are five tests.
    if passed == 5:
        print("Win!")
    else:
        print("Trouble!")