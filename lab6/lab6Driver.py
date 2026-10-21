# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 3/20/2026
import lab6
def main():
    sortedL1 = [1,2,3,34,55]
    sortedL2= [9,15,32,74,85,100,121,144,201,244]
    unsortedL1 = [32,55,12,87,5,100]
    unsortedL2 = [500,98,64,101,600,4,6,8]
    errorL1 = [1,3,'a',4]
    errorL2 = [5,2,4,6,7,'b']
    print(f'Linear search for 5 in unsortedL1 {unsortedL1}: {lab6.sequential_search(unsortedL1,5)}')
    print(f'Linear search for 101 unsortedL1 {unsortedL1} (Not Found): {lab6.sequential_search(unsortedL1,101)}')
    print(f'Smart Sequential search for 100 sortedL2 {sortedL2}: {lab6.smart_sequential_search(sortedL2,100)}')
    print(f'Smart Sequential search for 5 sortedL1 {sortedL1} (Not Found): {lab6.smart_sequential_search(sortedL1,5)}')
    try:
        print(f'Error in Smart Sequential search for errorL1 {errorL1}: {lab6.smart_sequential_search(errorL1,5)}')
    except ValueError:
        print(f'Value Error in smart sequential search for errorL1: {errorL1}')
    print(f'Binary search for 244 in sortedL2 {sortedL2}: {lab6.binary_search(sortedL2,244)}')
    print(f'Binary search for 74 in sortedL2 {sortedL2}: {lab6.binary_search(sortedL2,74)}')
    try:
        lab6.binary_search(errorL2,8)
    except ValueError:
        print(f'Value Error in binary seach for errorL2: {errorL2}')


if __name__ == "__main__":
    main()
