# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 2/20/2026
class Stack:
    """
    DO NOT change the name of the class. All class methods must have self as the first parameter.

    Implement the following methods:
    __init__(): the class constructor
    push(item): adds item to the top of the stack
    pop(): removes and returns the top item on the stack. Returns None if the stack is empty.
    peek(): returns the top item on the stack, but does not remove it. Returns None if the stack is empty.
    is_empty(): returns True if the stack is empty, False otherwise
    __len__(): supports calls to len(stack_object). returns the number of items in the stack
    """
    def __init__(self):
        self.stack = []
        
    def push(self,item):
        self.stack.insert(0,item)
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop(0)
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[0]
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)
    
    def __iter__(self): # return an iter object to be used to loop over in undoer.py
        return iter(self.stack)
    


if __name__ == '__main__':
    # You may add code below this line to help you test.


    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

    from tests import StackTests
    import sys
    suite = StackTests(sys.modules[__name__])
    suite.test_01_constructor()
    suite.test_02_push_pop()
    suite.test_03_pop_empty()
    suite.test_04_peek()
    suite.test_05_peek_empty()
    suite.test_06_is_empty()
    suite.test_07__len__()

