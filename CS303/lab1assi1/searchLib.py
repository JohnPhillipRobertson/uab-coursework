def lin_search(arr, target):
    count = 0
    for i in arr:
        if i == target:
            return count
        count += 1
    return -1

def bin_search(arr, target, m=0):
    if m == 0 and len(arr) == 1:
        return 0
    mid = m
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return bin_search(arr[mid:], target, mid + len(arr)//2)
    elif target < arr[mid]:
        return bin_search(arr[:mid-1], target, mid - len(arr)//2)
    else:
        return -1