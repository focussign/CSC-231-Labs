# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 2/6/2026
from fraction import Fraction

def main():
    a = Fraction(3,4)
    b = Fraction(1,2)
    c = Fraction(-8,20)
    d = Fraction(6,32)
    print(f'printing fraction: {a}')
    print(f'printing fraction: {d}')
    print(f'neg fraction dunder: {-a}')
    a.setNumerator(3)
    a.setDenominator(4)
    print(f'Used setter method: {a}')
    print(f'Reduce basic: {d.reduce()}')
    print(f'Reduce negative: {c.reduce()}')
    print(f'Addition: {a+d}')
    print(f'Addition with negative: {b+c}')
    print(f'Subtraction: {a-b}')
    print(f'Subtraction with neg: {c-d}')
    print(f'multiplication: {a*b}')
    print(f'multiplication with negative: {b*c}')
    print(f'division: {a/b}')
    print(f'division with negative number: {c/d}')
    print(f'== equality: {a == b}')
    e = Fraction(3,4)
    print(f'== equality: {a == e}')
    print(f'!= equality: {a != b}')
    print(f'!= equality: {a != e}')
    print(f'< equality: {a < b}')
    print(f'< equality: {b < a}')
    print(f'<= equality: {b <= c}')
    print(f'<= equality: {a <= e}')
    print(f'> equality: {a > b}')
    print(f'> equality: {c > b}')
    print(f'>= equality: {a >= c}')
    print(f'>= equality: {a >= e}')

    

if __name__ == '__main__':
    main()
