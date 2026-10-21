# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 3/27/2026
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return f'Node(data={self.data})'

class DoublyLinkedList:
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
            self.tail = self.head
            self.tail.prev = node
            self.head = node
            node.next = self.tail
        else:
            self.size +=1
            self.head.prev = node
            node.next = self.head
            self.head = node

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def append(self, item):
        node = Node(item)
        if not self.tail:
            self.tail = node
            if not self.head:
                self.head = node
        else:
            if self.size > 1:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                self.head = self.tail
                self.head.next = node
                node.prev = self.head
                self.tail = node
        self.size +=1

    def pop(self, pos = -1):
        if self.is_empty():
            raise IndexError
        elif type(pos) != type(1):
            raise TypeError
        elif pos > self.size:
            raise IndexError
        if pos == -1 and self.size > 1:
            val = None
            if not self.tail.next:
                val = self.tail.data
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                val = self.tail.data
                self.tail = None
            self.size-=1
            return val
        elif self.tail and pos > self.size //2:
            curNode = self.tail
            i = self.size-1
            if i == pos and curNode.prev:
                self.tail = curNode.prev
                self.tail.next = None
                self.size-=1
                return curNode.data
            while curNode.prev and i != pos:
                curNode = curNode.prev
                i-=1
            curNode.prev = curNode.next
            self.size-=1
            return curNode.data
        else:
            curNode = self.head
            i = 0
            if i == pos and curNode.next:
                self.head = curNode.next
                self.head.prev = None
                self.size-=1
                return curNode.data
            while curNode.next and i != pos:
                curNode = curNode.next
                i+=1
            if curNode.next:
                self.head.next = curNode.next
                self.head.next.prev = self.head
            else:
                self.head = None
                curNode.prev = curNode.next
            self.size-=1
            return curNode.data

    def search(self, item):
        if self.is_empty():
            return False
        l = self.head
        r = self.tail
        if self.head and self.tail:
            while l.next and r.prev and (l.data != item and r.data != item):
                l = l.next
                r = r.prev
            return l.data == item or r.data == item
        else:
            while l.data != item:
                l = l.next
            return l.data == item
            
            
    def remove(self, item):
        self.size -=1
        l = self.head
        r = self.tail
        if l.data == item:
            self.head = l.next
            if self.size == 0:
                self.head = None
                self.tail = None
                return
            if self.size == 1:
               self.tail = self.head
            self.head.prev = None
            l = None
            return
        if r and r.data == item:
           self.tail = r.prev
           self.tail.next = None
           r = None
           return
        if l and r:
            while l.next and r.prev and (l.data != item and r.data != item):
                l = l.next
                r = r.prev
            if l.data == item:
                l.prev.next = l.next
                l.next.prev = l.prev
            elif r.data == item:
                r.prev.next = r.next
                r.next.prev = r.prev
            else:
                raise ValueError
        elif l:
            while l.next and l.data != item:
                l = l.next
            l.prev = l.next
            l = None
            
                
        
if __name__ == '__main__': 
    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.
    from tests_ll import DLLTests
    import sys
    suite = DLLTests(sys.modules[__name__])
    suite.test_01_node_basic()
    suite.test_02_dll_init_is_empty()
    suite.test_03_add_basic_and_links()
    suite.test_04_append_basic_and_links()
    suite.test_05_append_to_empty()
    suite.test_06_iter_basic()
    suite.test_07_search()
    suite.test_08_remove_head_tail_middle_links()
    suite.test_09_remove_only_element_and_missing()
    suite.test_10_pop_tail_head_middle()
    suite.test_11_pop_errors_and_types()
