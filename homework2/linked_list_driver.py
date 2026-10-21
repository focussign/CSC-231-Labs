#################################
#
# Use this file to test your Linked List implementation. In a few places, it initializes names to either a new
# LinkedList. This file assumes that your LinkedList class is in a file called linked_list.py.
#
# You will probably want to comment out some of the test code as you build up your classes so that you can test them
# incrementally. Your Linked List methods are tested in the same order that they appear in the description
#################################

from linked_list import *

names = LinkedList()

print('List is empty? Should be True:', names.is_empty())
print('List size should be 0:', names.size)

names.add('Alice')
print('Added Alice to the list. Size should be 1:', names.size)
print('List is empty? Should be False:', names.is_empty())

names.add('Bob')
names.add('Charlie')
print('Added Bob and Charlie. Size should be 3:', names.size)
print('Order should be Charlie, Bob, Alice')
for x in names:
    print(x)


print('\nClearing the list')
names = LinkedList()
names.append('Harry')
print('Appended Harry to a new, empty list. Size should be 1:', names.size)

names.append('Hermione')
names.append('Ron')
print('Appended Hermione and Ron to the list. Order should be Harry, Hermione, Ron')
for x in names:
    print(x)

print('calling pop(). Should return Ron: {}, and the size should be 2: {}'.format(names.pop(), names.size))
print('calling pop(). Should return Hermione: {}, and the size should be 1: {}'.format(names.pop(), names.size))
print('calling pop(). Should return Harry: {}, and the size should be 0: {}'.format(names.pop(), names.size))

print('Appending some characters back to the list: McGonagall, Harry, Hermione, Ron, Snape')
names.append('McGonagall')
names.append('Harry')
names.append('Hermione')
names.append('Ron')
names.append('Snape')

print('calling pop(4). Should return Snape: {}, and the size should be 4: {}'.format(names.pop(4), names.size))
print('calling pop(0). Should return McGonagall: {}, and the size should be 3: {}'.format(names.pop(0), names.size))
print('calling pop(1). Should return Hermione: {}, and the size should be 2: {}'.format(names.pop(1), names.size))
print('List should now have Harry and Ron in that order.')
for x in names:
    print(x)

print('Searching for Harry. Should be True:', names.search('Harry'))
print('Searching for Ron. Should be True:', names.search('Ron'))

print('\nClearing the list')
names = LinkedList()
print('Appending some characters back to the list: McGonagall, Harry, Hermione, Ron, Snape')
names.append('McGonagall')
names.append('Harry')
names.append('Hermione')
names.append('Ron')
names.append('Snape')
names.remove('Snape')
print('called remove(\'Snape\'). Does not return anything, but list size should be 4:', names.size)
names.remove('McGonagall')
print('called remove(\'McGonagall\'). Does not return anything, but list size should be 3:', names.size)
names.remove('Hermione')
print('called remove(\'Hermione\'). Does not return anything, but list size should be 2:', names.size)
print('List should now have Harry and Ron in that order.')
for x in names:
    print(x)
