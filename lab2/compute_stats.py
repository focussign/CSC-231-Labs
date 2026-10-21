# Jack Trieu
# Professor Pulatov
# CSC 231, section 002
# 1/28/2026
def compute_stats(file):
   lst = []
   maximum = 0
   minimum = 0
   avg = 0
   with open(file, 'r') as numsFile: # All calculations done except median
        for line in numsFile:
            num = int(line) 
            lst.append(num)
            if(num > maximum):
                maximum = num
            if(num < minimum or len(lst)==1): # always initialize min as 1st num so it won't be 0
                minimum = num
            avg += num
   print(f'Count: {len(lst)}')
   print(f'Average: {avg/len(lst)}')
   print(f'Min: {minimum}')
   print(f'Max: {maximum}')
   lst.sort()
   if(len(lst) % 2 == 1): # mod to know if size is odd or even
       print(f'Median: {lst[len(lst)//2]}') # if odd the med is int div of the size by 2
   else:
       print(f'Median: {(lst[len(lst)//2]+lst[len(lst)//2-1])/2}') # add the number to the right and left of a even size list


    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

if __name__ == "__main__":
    compute_stats("numbers.txt")
    compute_stats("numbers2.txt")
    compute_stats("numbers6.txt")
    compute_stats("numbers7.txt")
    
from tests import ComputeStatsTests
import sys
suite = ComputeStatsTests(sys.modules[__name__])
suite.test_01_numbers("numbers.txt")
suite.test_02_numbers2("numbers2.txt")
suite.test_03_numbers6("numbers6.txt")
suite.test_04_numbers7("numbers7.txt")
    
