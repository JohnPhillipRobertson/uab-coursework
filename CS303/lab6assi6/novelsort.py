from lib import heap_sort

def novel_sort(A):
    def mymax(A):
        max = float("-inf")
        for i in A:
            if i > max:
                max = i
        return max
    def mymin(A):
        min = float("inf")
        for i in A:
            if i < min:
                min = i
        return min
    arr = A[:]
    i = 0
    while arr:
        a = mymin(arr)
        b = mymax(arr)
        if len(arr) != 1:
            A.insert(i, a)
            A.insert(i + 1, b)
            arr.remove(a)
            arr.remove(b)
            A.pop()
            A.pop()
        else:
            A.insert(i, a)
            arr.remove(a)
            A.pop()
        i += 1

def transaction_sort(A):
    arr = [x[-1:-9:-1] for x in A]
    for a in arr:
        new = ""
        for i in [-1 * x for x in range(1, 9)]:
            new += a[i]
        arr[arr.index(a)] = new
    heap_sort(arr)
    heap_sort(A)

