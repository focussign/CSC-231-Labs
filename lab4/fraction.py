# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 2/6/2026
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator > 0: # if less than or equal to 0 it will raise error
            self.denominator = denominator
        else:
            raise ValueError
        
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def getNumerator(self): # getters and setters
        return self.numerator
    
    def getDenominator(self):
        return self.denominator
    
    def setNumerator(self, numerator):
        self.numerator = numerator
        
    def setDenominator(self, denominator):
        self.denominator = denominator
        
    def __calcGCD(self):
        m = self.denominator
        n = self.numerator
        while  m % n != 0:
            oldM = m
            oldN = n
            m = oldN
            n = oldM % oldN
        return n
    
    def reduce(self):
        GCD = self.__calcGCD()
        if GCD > 0:
            self.numerator //= GCD
            self.denominator //= GCD
        else:
            self.numerator //= GCD*-1
            self.denominator //= GCD*-1
        return self
    
    def __neg__(self): # should return self to get neg result or else you get noneType
        self.numerator *= -1
        return self
        
    def __add__(self, other): # unlike the subtract dunder method this one uses get and setter methods
        if (self.getDenominator() != other.getDenominator()):
            self.setNumerator(self.getNumerator()*other.getDenominator())
            oldSelfDenominator = self.getDenominator()
            self.setDenominator(self.getDenominator()*other.getDenominator())
            other.setNumerator(other.getNumerator()*oldSelfDenominator)
            other.setDenominator(other.getDenominator()*oldSelfDenominator)
        return  Fraction(self.getNumerator()+other.getNumerator(), self.getDenominator()).reduce()
    
    def __sub__(self, other):
        if (self.denominator % other.denominator == 0): # if self.denom mod other.denom equal 0 we know other.denom is a factor of self.denom
            other.numerator *= (self.denominator//other.denominator) # multiples other numerator and denominator by self.denom//other.denom to get the factor to get other denom to equal self denom
            other.denominator *= (self.denominator//other.denominator)
        elif (other.denominator % self.denominator == 0): # if otherFrac.denom mod self.denom equal 0 we know self.denom is a factor of other.denom
            self.numerator *= (other.denominator//self.denominator) # multiples self numerator and denominator by other.denom//self.denom to get the factor to get other denom to equal self denom
            self.denominator *= (other.denominator//self.denominator)
        elif (self.denominator != other.denominator): # doesn't need to run if self.denom == other.denom
            self.numerator *= other.denominator
            self.denominator *= other.denominator
            other.numerator *= (self.denominator//other.denominator) # self.denom//other.denom give us the original self.denom
            other.denominator *= (self.denominator//other.denominator)
            
        return Fraction(self.numerator-other.numerator, self.denominator).reduce()
    
    def __mul__(self, other):
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator).reduce()
    
    def __truediv__(self, other):
        return Fraction(self.numerator*other.denominator, other.numerator*self.denominator).reduce()
    
    def __eq__(self, other):
        selfFrac = self.reduce()
        otherFrac = other.reduce()
        return selfFrac.getNumerator() == otherFrac.getNumerator() and selfFrac.getDenominator() == otherFrac.getDenominator()
    
    def __ne__(self, other):
        selfFrac = self.reduce()
        otherFrac = other.reduce()
        return selfFrac.getNumerator() != otherFrac.getNumerator() or selfFrac.getDenominator() != otherFrac.getDenominator()
    
    def __lt__(self, other):
        selfFrac = self.reduce()
        otherFrac = other.reduce()
        return selfFrac.getNumerator()/selfFrac.getDenominator() < otherFrac.getNumerator()/otherFrac.getDenominator() # test equality for each through which one has a bigger number using getter and setters
    
    def __le__(self, other):
        selfFrac = self.reduce()
        otherFrac = other.reduce()
        return selfFrac.getNumerator()/selfFrac.getDenominator() <= otherFrac.getNumerator()/otherFrac.getDenominator()
    
    def __gt__(self, other):
        selfFrac = self.reduce()
        otherFrac = other.reduce()
        return selfFrac.getNumerator()/selfFrac.getDenominator() > otherFrac.getNumerator()/otherFrac.getDenominator()
    
    def __ge__(self, other):
        selfFrac = self.reduce()
        otherFrac = other.reduce()
        return selfFrac.getNumerator()/selfFrac.getDenominator() >= otherFrac.getNumerator()/otherFrac.getDenominator()






if __name__ == "__main__":
    
    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

    from tests import FractionTests
    import sys
    suite = FractionTests(sys.modules[__name__])
    suite.test_01_constructor_basic()
    suite.test_02_constructor_negative_numerator()
    suite.test_03_constructor_denom_zero_error()
    suite.test_04_constructor_denom_negative_error()
    suite.test_05_reduce_basic()
    suite.test_06_reduce_negative()
    suite.test_07_addition_simple()
    suite.test_08_subtraction()
    suite.test_09_multiplication()
    suite.test_10_division()
    suite.test_11_equality_true_unreduced()
    suite.test_12_equality_false()
    suite.test_13_greater_than()
    suite.test_14_less_than()
    suite.test_15_comparison_equal()
