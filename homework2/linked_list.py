# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 3/27/2026
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return f'Node(data={self.data})'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return not bool(self.size)

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.size +=1
            self.head = node
        elif self.size == 1:
            self.size +=1
            prev = self.head
            self.head = node
            node.next = prev
            self.tail = prev
        else:
            self.size +=1
            prev = self.head
            node.next = prev
            self.head = node

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.size +=1
            self.head = node
            self.tail = node
            return
        self.size +=1
        if not self.head:
            self.head = self.tail
            self.head.next = node
            self.tail = self.head.next
        else:
            self.tail.next = node
            self.tail = node

    def pop(self, pos=-1):
        if self.is_empty():
            raise IndexError
        elif pos > self.size:
            raise IndexError
        elif type(pos) != type(1):
            raise TypeError
        cur = self.head
        prev = None
        i = 0
        self.size-=1
        if i == pos and cur.next:
            self.head = cur.next
            return cur.data
        elif i == pos and self.size == 1:
            self.head = None
            self.tail = None
            return cur.data
        while cur.next and i != pos and self.size >=1:
            prev = cur
            cur = cur.next
            i+=1
        if cur.next:
            prev.next = cur.next
        elif self.size >= 1:
            self.tail = prev
            self.tail.next = None
        else:
            self.tail = None
            self.head = None
        return cur.data

    def search(self, item):
        if self.is_empty():
            return
        cur = self.head
        while cur:
            if cur.data == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        if self.is_empty():
          return
        elif self.size == 1:
            self.tail = None
        self.size -=1
        if self.head and self.head.data == item:
            used = self.head
            self.head = self.head.next
            used = None
        elif self.tail and self.tail.data == item:
            cur = self.head
            prev = None
            while cur.next != None:
                prev = cur
                cur = cur.next
            self.tail = prev
            prev.next = None
        else:
            cur = self.head
            prev = None
            while cur.next and cur.data != item:
                prev = cur
                cur = cur.next
            if cur.next != None:
                prev.next = cur.next
            else:
                raise ValueError

        
            
                
            
        
            
        

    
    
if __name__ == '__main__': 
    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.
    from tests_ll import LLTests
    import sys
    suite = LLTests(sys.modules[__name__])
    suite.test_01_node_basic()
    suite.test_02_ll_init_is_empty()
    suite.test_03_add_basic()
    suite.test_04_append_basic()
    suite.test_05_append_to_empty()
    suite.test_06_iter_basic()
    suite.test_07_search()
    suite.test_08_remove_head_tail_middle()
    suite.test_09_remove_only_element_and_missing()
    suite.test_10_pop_default_and_indices()
    suite.test_11_pop_errors_and_types()
