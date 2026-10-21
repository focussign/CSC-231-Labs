# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 3/20/2026
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True, i
    return False, None

def is_valid(arr):
    if not len(arr):
        return False
    if type(arr[0]) == type(1):
        for i in arr:
            if type(i) != type(1):
                raise ValueError
        return True  
    elif type(arr[0]) == type(1.5):
        for i in arr:
            if type(i) != type(1.5):
                raise ValueError
        return True
    else:
        raise ValueError
            
def smart_sequential_search(arr, target):
    if is_valid(arr):
        for i in range(len(arr)):
            if arr[i] == target:
                return True, i
            elif arr[i] > target:
                return False, None
    return False, None

def binary_search(arr, target):
    if is_valid(arr):
        lo = 0
        hi = len(arr)-1
        med = lo + (hi-lo)//2
        while lo <= hi:
            if arr[med] == target:
                return True, med
            elif arr[med] > target:
                hi = med-1
            elif arr[med] < target:
                lo = med+1
            med = lo + (hi-lo)//2
        return False, None
            
                


        
if __name__ == "__main__":
    # You may add code below this line to help you test.


    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.
    from tests import SearchTests
    import sys
    suite = SearchTests(sys.modules[__name__])
    suite.test_01_sequential_found()
    suite.test_02_sequential_not_found()
    suite.test_03_smart_found()
    suite.test_04_smart_not_found()
    suite.test_05_smart_type_error()
    suite.test_06_binary_found()
    suite.test_07_binary_not_found()
    suite.test_08_binary_type_error()
