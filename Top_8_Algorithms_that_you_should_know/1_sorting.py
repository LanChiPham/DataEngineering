## 1. Sorting algorithms:
# Quick sort is a divide-and-conquer algorithm that chooses a "pivot" element from the array and partitions the other elements into two sub-arrays , according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively

def quicksort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [ x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print (f"Quick sort:")
print (quicksort([3,6,8,10,1,2,1])) # [1, 1, 2, 3, 6, 8, 10]

## Merge sort: the merge sort algorithm is a divide-and-conquer algorithm that divides an array in two, sorts the two halves, and then merge them back together.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    i = 0 
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

    result += left[i:]
    result += right[j:]
    return result 

print (f"Merge sort: ")
print (merge_sort([3,6,8,10,1,2,1])) # [1, 1, 2, 3, 6, 8, 10]


# Heap sort: The heap sort algorithm is a comparison-based sorting algortihm that builds a heap from the input elements and then repeatedly extracts the maximum element from the heap and places it at the end of the sorted ouput array.

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


print (f"Heap sort:")
print(heap_sort([3,6,8,10,1,2,1])) # none 