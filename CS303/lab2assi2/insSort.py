from random import randrange

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

def main():
    #The following tests random elements
    errors = 0
    for k in range(100):
        a = [randrange(1, 400) for i in range(400)]
        b = a[:]
        a.sort()
        if ins_sort(b) != a:
            print("trouble")
            print(str(ins_sort(b) == a))
            errors += 1
    if errors == 0:
        print("True")
    #Test on zero elements
    emptyArr = []
    e = emptyArr[:]
    e.sort()
    print(ins_sort(emptyArr) == e)
    #Test on reverse sorting
    revSorted = [5, 4, 3, 2, 1]
    r = revSorted[:]
    r.sort()
    print(ins_sort(revSorted) == r)
    #Test on one element
    oneElem = [1]
    o = oneElem[:]
    o.sort()
    print(ins_sort(oneElem) == o)

if __name__ == "__main__":
    main()
