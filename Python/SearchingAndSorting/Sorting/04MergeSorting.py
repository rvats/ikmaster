def mergeSort(array):
    start, end = 0, len(array)-1
    return mergeSortHelper(array, start, end)

def mergeSortHelper(array, start, end):
    if start == end-1:
        if array[start] > array[end]:
            array[start], array[end] = array[end], array[start]
    elif end > start:
        mid = start + (end-start)//2
        mergeSortHelper(array, start, mid)
        mergeSortHelper(array, mid+1, end)
    return array

array = [10, 8, 6, 4, 2]
print(mergeSort(array))