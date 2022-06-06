def BinarySearch(array, value):
    # i will use high,mid,low as pointers to move through the array
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        #used to split the array in half
        if array[mid] < value:
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1


x = [11, 22, 33, 44, 55, 66, 77]
print(BinarySearch(x, 5))

