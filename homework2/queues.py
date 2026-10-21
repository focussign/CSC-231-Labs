# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 3/27/2026
from doubly_linked_list import DoublyLinkedList
class QueuePythonList:
    """
    DO NOT change the name of the class. All class methods must have self as the first parameter.

    Implement the following methods:
    __init__(): the class constructor
    enqueue(item): adds item to the rear of the queue
    dequeue(): removes and returns the item at the front of the queue. Returns None if the queue is empty.
    is_empty(): returns True if the queue is empty, False otherwise
    __len__(): supports calls to len(queue_object). returns the number of items in the queue
    """
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def __len__(self):
        return len(self.queue)

class QueueLinkedList:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def enqueue(self, item):
        self.dll.append(item)

    def dequeue(self):
        try:
            return self.dll.pop(0) 
        except IndexError:
            return None

    def is_empty(self):
        return self.dll.is_empty()

    def __len__(self):
        return self.dll.size

if __name__ == '__main__':
    # You may add code below this line to help you test.

    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.

    from tests_queue import QueueTests
    import sys

    print("===== Testing QueuePythonList =====")
    suite = QueueTests(sys.modules[__name__], "QueuePythonList")
    suite.test_01_constructor()
    suite.test_02_enqueue_dequeue()
    suite.test_03_dequeue_empty()
    suite.test_04_is_empty()
    suite.test_05__len__()

    print("\n===== Testing QueueLinkedList =====")
    suite = QueueTests(sys.modules[__name__], "QueueLinkedList")
    suite.test_01_constructor()
    suite.test_02_enqueue_dequeue()
    suite.test_03_dequeue_empty()
    suite.test_04_is_empty()
    suite.test_05__len__()
