# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 2/2/2026
    # You may add code below this line to help you test.
class FootMeasure:
    def __init__(self, feet = 0, inches = 0):
        self.feet = feet
        self.inches = inches
        while self.inches >= 12:
            self.feet +=1
            self.inches -= 12
    def __str__(self):
        return f'{self.feet} ft. {self.inches} ins.'
    def __add__(self, other):
        return FootMeasure(self.feet + other.feet, self.inches + other.inches)
    def __eq__(self, other):
        return self.feet == other.feet and self.inches == other.inches
    def __ne__(self, other):
        return self.feet != other.feet or self.inches != other.inches
    def __lt__(self, other):
        return self.feet < other.feet or (self.feet == other.feet and self.inches < other.inches)
    def __le__(self, other):
        return self.feet <= other.feet or (self.feet == other.feet and self.inches <= other.inches)
    def __gt__(self, other):
        return self.feet > other.feet or (self.feet == other.feet and self.inches > other.inches)
    def __ge__(self, other):
        return self.feet >= other.feet or (self.feet == other.feet and self.inches >= other.inches)

        

    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.
if __name__ == "__main__":
    from tests import FootMeasureTests
    import sys
    suite = FootMeasureTests(sys.modules[__name__])
    suite.test_01_zero_measure()
    suite.test_02_simple_measure()
    suite.test_03_inches_only()
    suite.test_04_normalization()
    suite.test_05_addition_simple()
    suite.test_06_addition_with_carry()
    suite.test_07_equality_true()
    suite.test_08_equality_false()
    suite.test_09_greater_than()
    suite.test_10_less_than()
    suite.test_11_greater_equal_and_less_equal()
