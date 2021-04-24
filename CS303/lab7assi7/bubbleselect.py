from time import perf_counter as perf

def bubble_sort(A):
    for i in range(len(A) - 1):
        j = len(A) - 1
        while j >= i + 1:
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]
            j -= 1

def selection_sort(A):
    for i in range(len(A) - 1):
        min = i
        j = i + 1
        while j < len(A):
            if A[j] < A[min]:
                min = j
            j += 1
        if i != min:
            A[min], A[i] = A[i], A[min]



def main():
    files = ["Input_Random.txt", "Input_ReversedSorted.txt", "Input_Sorted.txt"]
    tupni = input("Would you like to test the three big files? Press '1' if so.")
    if tupni == '1':
        for file in files:
            inputFile = open(file, "r")
            inputs = inputFile.read()
            inputs = inputs.lstrip()
            inputs = inputs.split()
            inputFile.close()
            sort1 = [int(i) for i in inputs if i != ' ']
            sort2 = [int(i) for i in inputs if i != ' ']
            sort3 = [int(i) for i in inputs if i != ' ']
            start = perf()
            bubble_sort(sort1)
            print("Performance on {} for bubble sort: {}".format(file, perf() - start))
            start = perf()
            selection_sort(sort2)
            print("Performance on {} for selection sort: {}".format(file, perf() - start))
            start = perf()
            sort3.sort()
            print("Performance on {} for library sort: {}".format(file, perf() - start))

    passed = 0
    l = [4, 4, 7, 5, 9, 14, 15, 14]
    r = l[:]
    u = l[:]
    l.sort()
    selection_sort(r)
    bubble_sort(u)
    if l == r and r == u:
        passed += 1
    else:
        print("library")
        print(l)
        print("selection")
        print(r)
        print("bubble")
        print(u)
    #random elements and library sort
    from random import randrange
    sortie = [randrange(16) for i in range(8)]
    sorted = sortie[:]
    sartorial = sortie[:]
    sortie.sort()
    bubble_sort(sorted)
    selection_sort(sartorial)
    if sortie == sorted and sortie == sartorial:
        print("Simple test passed")
        passed += 1
    else:
        print("library")
        print(sortie)
        print("bubble")
        print(sorted)
        print("selection")
        print(sartorial)
    #More random elements
    sortie = [randrange(512) for i in range(512)]
    sorted = sortie[:]
    sartorial = sortie[:]
    sortie.sort()
    bubble_sort(sorted)
    selection_sort(sartorial)
    if sortie == sorted and sortie == sartorial:
        print("Big test passed")
        passed += 1
    else:
        print("library")
        print(sortie)
        print("bubble")
        print(sorted)
        print("selection")
        print(sartorial)
    #No elements
    empty = []
    try:
        bubble_sort(empty)
        selection_sort(empty)
        print("Empty test passed")
        passed += 1
    except:
        print("Looks like that didn't work.")
    #Already sorted
    sortie = [i for i in range(512)]
    sorted = sortie[:]
    sartorial = sortie[:]
    sortie.sort()
    bubble_sort(sorted)
    selection_sort(sartorial)
    if sortie == sorted and sortie == sartorial:
        print("Already sorted test passed")
        passed += 1
    #There are five tests.
    if passed == 5:
        print("Win!")
    else:
        print("Trouble!")


if __name__ == "__main__":
        main()
