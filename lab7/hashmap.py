# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 4/2/2026
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size = 3):
        self.size = size
        self.table = [None] * size
        self.keys = []

    def __setitem__(self, key, value):
        self.index = 0
        if type(key) != type(1):
            self.index = self.strToInt(key)
        self.index %= self.size
        if not self.table[self.index]:
            self.table[self.index] = Node(key, value)
            self.keys.append(key)
        else:
            if key in self.keys and self.table[self.index].key == key:
                self.table[self.index].value = value
            elif key in self.keys:
                self.cur = self.table[self.index]
                while self.cur.next != None and self.cur.key != key:
                    self.cur = cur.next
                self.cur.value = value
            else:
                self.cur = self.table[self.index]
                while self.cur.next != None:
                    self.cur = self.cur.next
                self.cur.next = Node(key, value)
                self.keys.append(key)

    def __getitem__(self, key):
        if not key in self.keys:
            raise KeyError
        self.index = 0
        if type(key) != type(1):
            self.index = self.strToInt(key)
        self.index %= self.size
        if self.table[self.index].key == key:
            return self.table[self.index].value
        else:
            self.cur = self.table[self.index]
            while self.cur.next != None and self.cur.key != key:
                self.cur = self.cur.next
            return self.cur.value

    def __delitem__(self, key):
        if not key in self.keys:
            raise KeyError
        self.index = 0
        if type(key) != type(1):
            self.index = self.strToInt(key)
        self.index %= self.size
        if self.table[self.index].key == key:
            self.table[self.index] = None
            self.keys.remove(key)
        else:
            self.cur = self.table[self.index]
            self.prev = None
            while self.cur.next != None and self.cur.key != key:
                self.prev = self.cur
                self.cur = self.cur.next
            if self.cur.next:
                self.prev.next = self.cur.next
                self.keys.remove(key)
                self.cur = None
            else:
                self.keys.remove(key)
                self.cur = None

    def __contains__(self, key):
        return key in self.keys

    def get_keys(self):
        return self.keys
                
        

    def strToInt(self, string):
        self.s = 0
        for i in string:
            self.s += ord(i)
        return self.s
            
if __name__ == '__main__': 
    # You may add code below this line to help you test.
    hm = HashMap(10)
    hm['a'] = 1
    hm['b'] = 2
    hm['d'] = 4
    hm['f'] = 6
    hm['e'] = 5
    print(f'printing key \'b\' value: {hm["b"]}')
    hm['a'] = 11
    hm['k'] = 14
    print(f'Collision with the same key \'a\': {hm["a"]}')
    print(f'Collision with different key \'k\': {hm["k"]}')
    print(f'keys: {hm.get_keys()}')
    del hm['b']
    print(f'deleting key \'b\' key in hm: {"b" in hm}')
    print(f'keys: {hm.get_keys()}')

    # You may comment out the calls to the test_xxx() functions to reduce the amount printed to the screen as you work.
    # Uncomment them when you are ready to test.
    from tests import HashMapTests
    import sys
    suite = HashMapTests(sys.modules[__name__])
    suite.test_01_set_and_get()
    suite.test_02_overwrite_value()
    suite.test_03_contains()
    suite.test_04_getitem_key_error()
    suite.test_05_delete_existing_key()
    suite.test_06_delete_missing_key_error()
    suite.test_07_get_keys_content()
    suite.test_08_collision_handling()
