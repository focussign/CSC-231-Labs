# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 2/20/2026
class Deque:
    """
    DO NOT change the name of the class. All class methods must have self as the first parameter.

    Implement the following methods:
    __init__(): the class constructor
    add_front(item): adds item to the front of the deque
    add_rear(item): adds item to the rear of the deque
    remove_front(): removes and returns the item at the front of the deque. Returns None if the deque is empty.
    remove_rear(): removes and returns the item at the rear of the deque. Returns None if the deque is empty.
    is_empty(): returns True if the queue is empty, False otherwise
    __len__(): supports calls to len(dequeue_object). returns the number of items in the deque
    """
    def __init__(self):
        self.deque = []
    def add_front(self, item):
        self.deque.insert(0,item)
    def add_rear(self, item):
        self.deque.append(item)
    def remove_front(self):
        if self.is_empty():
            return None
        else:  
            return self.deque.pop(0)
    def remove_rear(self):
        if self.is_empty():
            return None
        else:
            return self.deque.pop()
    def is_empty(self):
        return len(self.deque) == 0
    def __len__(self):
        return len(self.deque)


if __name__ == '__main__':
    # You may add code below this line to help you test.

    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

    from tests import DequeTests
    import sys

    suite = DequeTests(sys.modules[__name__])
    suite.test_01_constructor()
    suite.test_02_adds_and_removes()
    suite.test_03_remove_empty()
    suite.test_04_is_empty()
    suite.test_05__len__()
