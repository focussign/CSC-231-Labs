# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 4/15/2026
def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

def selection_sort(arr):
    for i in range(0, len(arr)):
        small = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[small]:
                small = j
        arr[small], arr[i] = arr[i], arr[small]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        n = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > n:
            arr[pos] = arr[pos-1]
            pos -=1
        arr[pos] = n  
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:len(arr)])
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        while i < len(left) or j < len(right):
            if i < len(left):
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
    return arr

def quick_sort(arr):
    quick_sort_helper(arr,0,len(arr)-1)
    return arr

def quick_sort_helper(arr, first, last):
    if first < last:
        split = partition(arr, first, last)
        quick_sort_helper(arr, first, split-1)
        quick_sort_helper(arr, split+1, last)

def partition(arr, first, last):
    pivotvalue = arr[first]
    i = first+1
    j = last
    done = False
    while not done:
        while i <= j and arr[i] <= pivotvalue:
            i = i + 1
        while arr[j] >= pivotvalue and j >= i:
            j = j - 1
        if j < i:
            done = True
        else:
            arr[i], arr[j] = arr[j], arr[i]
    arr[first], arr[j] = arr[j], arr[first]
    return j

if __name__ == "__main__":
    # You may add code below this line to help you test.
    print('****************DRIVER TEST BELOW****************')
    testArr = [57, 3, 91, 24, 68, 12, 105, 44, 7, 83]
    print(f'Original arr:{testArr} bubble_sort:{bubble_sort(testArr)}')
    print(f'Original arr:{testArr} selection_sort:{selection_sort(testArr)}')
    print(f'Original arr:{testArr} insertion_sort:{insertion_sort(testArr)}')
    print(f'Original arr:{testArr} merge_sort:{merge_sort(testArr)}')
    print(f'Original arr:{testArr} quick_sort:{quick_sort(testArr)}')

    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.
    from tests import SortingTests
    import sys
    suite = SortingTests(sys.modules[__name__])
    suite.test_01_bubble_basic()
    suite.test_02_bubble_edge_cases()
    suite.test_03_selection_basic()
    suite.test_04_selection_edge_cases()
    suite.test_05_insertion_basic()
    suite.test_06_insertion_edge_cases()
    suite.test_07_merge_basic()
    suite.test_08_merge_edge_cases()
    suite.test_09_quick_basic()
    suite.test_10_quick_edge_cases()
