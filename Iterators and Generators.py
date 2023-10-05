#Iterators
'''
1. Iterators and generators are important concepts in Python that help manage and manipulate sequences of data efficiently. 
2. They play a significant role in improving memory usage and optimizing code execution when working with large datasets 
    or when you need to generate sequences on-the-fly.

#Iterators:
1. An iterator is an object that allows you to loop through a collection of data, such as a list or a dictionary, one element at a time. 
2. It provides methods like __iter__() and __next__() to traverse the elements sequentially. 
3. The __iter__() method returns the iterator object itself, and the __next__() method retrieves the next element in the sequence.

a = [1,2,3,4,5]

a = a.__iter__()
print(next(a))
print(next(a))
print(next(a))

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value

        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
iterator = MyIterator(my_list)

for item in iterator:
    print(item)

    
#Generators:
1. Generators are a more concise and memory-efficient way to create iterators.
2. A generator function contains one or more yield statements, which temporarily suspends the function's execution and yields a value to the caller. 
3. When the generator is iterated, the function resumes execution from where it was paused and continues generating values.

def my_generator(data):
    for item in data:
        yield item

my_list = [1, 2, 3, 4, 5]

for item in my_generator(my_list):
    print(item)

'''

from array import *
arr =  array('f',[1,2,3.0,4])
print(arr[3])
print(type(arr))