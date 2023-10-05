#Zip Function
#zip is used to combine two or more iterables (e.g., lists or tuples) into a single iterable, creating pairs of corresponding elements from each input iterable.
#It takes multiple iterable arguments and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
'''
l1 = [1,2,3,4]
l2 = ['a','b','c','d']

#for i in range(len(l1)):
#    print(l1[i], l2[i])

zipped = zip(l1, l2)
print(list(zipped))


company = ['Samsung', 'Nokia', 'Iphone']
Location = ['Germany', 'Japan', 'America']

zipped = zip(company, Location)
print(list(zipped))

#for i, j in zipped:
#    print(f'My mobile is {i} and it\'s headquater located in {j}')
    

unzip = zip(*zipped)
print(list(unzip))

#enumerate()
#enumerate is used to iterate over elements of an iterable while keeping track of the index (position) 
# of each element. 
#It returns an iterator of tuples where each tuple contains two values: the index (starting from 0 by default) 
# and the corresponding element from the iterable.

#Syntax: enumerate(iterable, start=0)

l1 = ('Google', 'Nokia', 'Samsung', 'Google', 'Samsung', 'Google', 'Google', 'GOOGLE')
print(l1.index('Google')) # 0

enum = enumerate(l1,0)
for i,j in enum:
    if j =='Google':
        print(i,j)

#lamda()
#They are also referred to as anonymous functions sometimes. The syntax for lambda functions is as follows:
#Syntax: lambda arguments : expression

#Lambda functions can have any number of arguments but can only have one expression. 
#They are often used when you need a simple function for a short period of time 
# and don't want to define a full function using the def keyword.

#Print Hello world
def my_func():
    return 'Helloworld'
print(my_func())

#Print Hello world using Lambda
print((lambda: 'Helloworld')())

#Print Hello world using Lambda
x = (lambda: 'Helloworld')
print(x())

#Print Firstname and Lastname

first_name= 'Techie'
Last_name = 'Smiles'
print (f'Hello, {first_name} {Last_name}')

#Lambda function

x = lambda first_name, Last_name: f'Hello, {first_name} {Last_name}'
print(x('Ida', 'Jones'))


#Check the name and print the result

def func(name):

    if name[0] == 'A' or name[0] == 'a':
        print(f'Hi {name}, welcome')
    else:
        print('Name should always starts with A')

func('Arun')
func('Raiza')

#Lambda function

x = lambda name: f'Hi {name}, welcome' if name[0] == 'A' or name[0] == 'a' else 'Name should always starts with A'
print(x('Azar'))


#Addition using lambda
x= lambda *args: sum(args)
print(x(2,3,4,5))

# Print Even and Odd numbers
for i in range(1,11):
    if i%2 ==0:
        print(f'{i} Even numbers')
    else:
        print(f'{i} Odd Number')

x = lambda i:  [f'{i} Even numbers' if i%2 ==0 else f'{i} Odd Number' for i in range(1,11)  ]
print(x(i))


# Map function

#The map() function in Python is used to apply a given function to each item in an iterable 
#(such as a list, tuple, or other iterable) and returns a new iterable with the results. 

#It takes two or more arguments:
#A function: The function that you want to apply to each item in the iterable.
#One or more iterable(s): The iterable(s) whose elements you want to process using the function.

#Syntax:
#map(function, iterable, ...)

def square(x):
    return x+1

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the result to a list (or another iterable if needed)
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]


#Map function for multiple iterables
salary = [('Arun', 10000),('Aravind', 13200),('Ashok', 23000)]

x = map(lambda x: (x[0],x[1]+100), salary)
for i in x:
    print(i)


# If condition using map function

numbers = [1,2,3,4,5]
# Using lambda with filter
even_numbers = list(map(lambda x: x%2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

'''
# Filter()
#The filter() function in Python is used to filter elements from an iterable 
#(such as a list, tuple, or other iterable) based on a specified condition. 

#It takes two arguments:
#1. A function: The function that defines the condition for filtering. 
#This function should return True for elements you want to keep and False for elements you want to discard.

#2. An iterable: The iterable from which you want to filter elements.
#The basic syntax of the filter() function is as follows: filter(function, iterable)

numbers = [1,2,3,4,5]
# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


numbers = [1,2,3,4,5]
# Using lambda with filter
even_numbers = list(map(lambda x: x%2 == 1, numbers))
print(even_numbers)  # Output: [2, 4]

# Print the values which are greater than len(3)
strings = ['one', 'two', 'three', 'four', 'five', 'six']

filtered_strings = filter(lambda string: len(string) > 3,
strings)

print(list(filtered_strings)) # Output :['four','five','six']