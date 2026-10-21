# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 2/20/2026
from stack import Stack
class undoer:
    def __init__(self, filename):
        self.fn=filename
        self.s = Stack()
        self.undo()
        
    def undo(self):
        with open(self.fn, 'r') as f:
           for line in f:
               for c in line: # gets individual chars for each line
                   if c !=  '<':
                       self.s.push(c)
                   else:
                       self.s.pop()
                       
    def __str__(self):
        string = ''
        for c in self.s:
            string += c
        return string[::-1] # slices get the reverse
            

if __name__ == "__main__":
    undo1 = undoer('undo/undo1.txt')
    undo2 = undoer('undo/undo2.txt')
    undo3 = undoer('undo/undo3.txt')
    print(f'undo1: {undo1}\nundo2: {undo2}\nundo3: {undo3}')
    
