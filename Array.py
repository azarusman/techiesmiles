# Array?
'''
An array can be thought of as a container that can hold a fixed number of data values of the same type.
An array consists of two components, viz Element and Index.

• Element: These are the actual data values to be stored in an array.
• Index: Each element in array is positioned at the particular location depicted by an index. 
    Python follows zero based indexing which meansan index will always start with 0

Syntax: array('typecode',[])

What is Typecode?
https://docs.python.org/3/library/array.html?highlight=array#module-array

from array import *

arr = array('u', ['a','b','c'])
print(type(arr))
print(arr)

arr1 = array('i', [1,2,3,4,5,6,-1])
print(type(arr1))
print(arr1)

arr2 = array('I', [1,2,3,4,5,6])
print(type(arr2))
print(arr2)

arr3 = array('f', [1,2,3,4,5.5])
print(type(arr3))
print(arr3)

arr4 = array('i',[11,12,13,14,15])
print(type(arr4))
print(arr4)

#arr5 = array('u', ['aa','bb','cc'])
#print(type(arr5))
#print(arr5)

# Array Operations
# Accessing a value in array

from array import *

arr = array('u', ['a','b','c'])
print(arr[0])       # Output: a

arr1 = array('i', [1,2,3,4,5,6,-1])
print(arr1[5])      # Output: 6

arr3 = array('u', ['d','e'])

# Inserting a value at a particular index position
arr1.insert(0,9)
print(arr1)

arr.insert(3,'d')
print(arr)

# Delete/Pop a particular value in Index position
arr.pop()
print(arr)

arr.pop(1)
print(arr)

# Appending a particular value
arr.append('a')
print(arr)

arr1.append(9)
print(arr1)

# Counting a particular value
a = arr.count('a')
print(a)

# Removing a value
arr.remove('a')
print(arr)

# Extend an array
arr.extend(arr3)
print(arr)

# Stack
In Python, you can implement a stack data structure using a list. 
A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed. 

Here's how you can create a stack in Python using a list:

stack = [1,2,3,4,5]
print(stack[0])
print(type(stack))

print(stack[::-1])
print(stack[:-1])

from collections import deque
stack = deque()

stack.append(1)
print(stack)
print(type(stack))

stack.append(1)
stack.appendleft('a')
print(stack)

stack.appendleft('A')
print(stack)

stack.pop()
print(stack)

stack.remove('A')
print(stack)

# Queue

In Python, you can implement a queue data structure using various approaches. 
One common approach is to use the collections module, which provides the deque class (double-ended queue) for efficient queue operations. 
Here's how you can create a queue using deque:
'''
from collections import *

queue = deque()

queue.appendleft('a')
queue.appendleft('A')
queue.appendleft(2)

print(queue) # deque([2, 'A', 'a'])

print(queue.pop())
print(queue.pop())


class queues:

    def __init__(self):
        self.buffer=deque()

    def enque(self,value):
        self.buffer.appendleft(value)

q = queues()
q.enque('a')
print(q)

