#Python Collections

#Data Structures
'''
1. In Python, a data structure is a way to organize and store data in memory to efficiently perform operations on that data. 
2. Data structures are essential for managing and manipulating data in various algorithms and applications. 
3. Python provides several built-in data structures, as well as support for creating custom data structures.

Some of the most commonly used built-in data structures in Python include:
List, Tuples, SET, Dictionary

# List, Tuples, SET, Dictionary

#List 
#What is List?

1. Ordered / Index based / Duplicate data allowed / Dynamic*
2. Lists are ordered collections of items that can store elements of different data types. 
3. They are mutable, which means you can modify, add, or remove elements after creation. 
4. Lists are defined using square brackets []

#Let's create a list:

Cars = ['BMW','VOLVO',12,12.5,12.5,True, True,'VOLVO'] 
print(Cars)

print(Cars.count('VOLVO'))
print(Cars.index('VOLVO'))

#How to dispaly a particular value based on the Index position from a list
print(Cars[3]) #12.5
print(Cars[0]) #BMW

#List - Data slicing
print(Cars[0:4]) # ['BMW', 'VOLVO', 12, 12.5]
print(Cars[0:]) #['BMW', 'VOLVO', 12, 12.5, 12.5, True, True, 'VOLVO']

#print the last 3 words 
print(Cars[-4:-1]) #[12.5, True, True]
print(Cars[-3:-1]) #[True, True]
print(Cars[-3:]) #[True, True, 'VOLVO']  - Corect answer
 

#Note: List will allow all kind of data types.


#List Append()
#Append() Method - Adds an element to end of the existing list. It takes only one argument i.e., new_element.

cars = ['BMW','VOLVO','12','12.5',True] 

#Appending a single value
cars.append('Jaguar')
print(cars) #['BMW', 'VOLVO', '12', '12.5', True, 'Jaguar']

#Adding Multiple Values in existing list
cars.append(12,12.5,'Suzuki') #TypeError: append() takes exactly one argument (3 given)
print(cars)


#cars.append('Jaguar', 'LandRover')
#cars.append('jaguar')
#print(cars)

#Multiple append
#cars.append(['','',''])

#List Pop()
#'pop()' method removes item based on the index position from the list. If no index is specified, it will remove the last item. 

cars = ['BMW','VOLVO','12','12.5',True] 
print(cars)

cars.pop() # Output ['BMW', 'VOLVO', '12', '12.5']
print(cars)

cars.pop() # Output  ['BMW', 'VOLVO', '12'] 
print(cars)

cars.pop(0) # Output ['VOLVO', '12']
print(cars) 

# Note: Once the value is deleted, the index will be re-arranged automatically.


#List Insert()
#(index,value) method adds given item at specified position in the list and shifts every subsequent
#item to the right by one slot. If no parameter for "position" provided then it inserts as
#last element (default behavior). The syntax used here is insert().

cars = ['BMW','VOLVO',12,12.5,True] 

cars.insert(0,1) #Syntax insert(Index Position, Value)
print(cars)#[1, 'BMW', 'VOLVO', '12', '12.5', True]

cars.insert(5,'Volvo')
print(cars) #[1, 'BMW', 'VOLVO', 12 ,12.5, 'Volvo', True]

cars.insert(8,'VOLVO')
print(cars) #[1, 'BMW', 'VOLVO', 12, 12.5, 'Volvo', True, 'VOLVO']
#Note: If the mentioned index position is not available, then the value will be added at the end of the list.

print(cars[7]) #VOLVO
print(cars[8]) #IndexError: list index out of range


#List length
cars = ['BMW','VOLVO', 'VOLVO','VOLVO','Volvo',12,12.5,True] 
print(len(cars)) #8

#List Count
print(cars.count('BMW')) #1

#List Remove
cars.remove('VOLVO')  #['BMW', 'VOLVO', 'VOLVO', 'Volvo', 12, 12.5, True]
print(cars)

cars.remove('Train')
print(cars) #ValueError: list.remove(x): x not in list

#List Reverse()

cars = ['BMW','VOLVO', 'VOLVO','VOLVO','Volvo',12,12.5,True]
cars.reverse() #[True, 12.5, 12, 'Volvo', 'VOLVO', 'VOLVO', 'VOLVO', 'BMW']
print(cars)

#List delete()
del(cars) # del() will delete the entire list.
print(cars) #NameError: name 'cars' is not defined

# List Index()
#Index() will help to return the Index position of the first occurance of the value.
print(cars.index('VOLVO')) #4
print(cars)

#List Sort and Copy
cars = ['bmw', 'BMW', 'VOLVO','JAGUAR','Volvo']
cars.sort()
print(cars) #['BMW', 'JAGUAR', 'VOLVO', 'Volvo', 'bmw']

cars = [1,2,3,4,7,2,12,3] 
cars.sort()
print(cars) #[1, 2, 2, 3, 3, 4, 7, 12]

#Reverse string or any other string you want reverse here!

#cars = [0,1,2,4,3,5]
cars = ['a','b','c','d','A','C','B']  

cars.sort()
print(cars) # ['A', 'B', 'C', 'a', 'b', 'c', 'd']

cars.sort(reverse=True) # ['d', 'c', 'b', 'a', 'C', 'B', 'A']
print(cars)

##### --- Copy till this ----###
#Appending multiple values in the list

#Adding more than one value in a  List
a = ['car','bus','bike', 1,2,3,'2','3']

#1: Inserting multiple value inside the list Using append, List Concatenation, List Slicing + Operator & Comprehension
values_to_add = [2,3,1]
a.append(values_to_add)
print(a)  #['car', 'bus', 'bike', 1, 2, 3, '2', '3', [2, 3, 1]] #Nested list

#2:
a+=values_to_add  #['car', 'bus', 'bike', 1, 2, 3, '2', '3', [2, 3, 1], 2, 3, 1]
print(a)

#List Slicing '+' Operator
b = [1,2,3,7,8]
values_to_insert = [4,5,6,'seven']
position = 3
b = b[:position]+values_to_insert+b[position:]
print(b)  #[1, 2, 3, 4, 5, 6, 'seven', 7, 8]

#Reading a value from the Nested list
a = ['car','bus','bike', 1,2,3,[['1',2,3],'2','3']]
a.append([4,3,2,1,2,3])
print(a)  #['car', 'bus', 'bike', 1, 2, 3, [['1', 2, 3], '2', '3'], [4, 3, 2, 1, 2, 3]]

print(a[2]) #bike
print(a[6]) #[['1', 2, 3], '2', '3']
print(a[6][0]) #['1', 2, 3]
print(a[6][0][2]) #3
print(a[6][2]) #3

#Appending a value inside a Nested list
a[6].append('Hello')   ##adding element to nested lists
print(a)  #['car', 'bus', 'bike', 1, 2, 3, [['1', 2, 3], '2', '3', 'Hello'], [4, 3, 2, 1, 2, 3]]

#Appending a value inside a Nested list
a[6][0].append('Helloworld')
print(a)  #['car', 'bus', 'bike', 1, 2, 3, [['1', 2, 3, 'Helloworld'], '2', '3', 'Hello'], [4, 3, 2, 1, 2, 3]]

#Inserting a value inside the nested list
a.insert(6,['Value1',1,2,3,'Value2'])
print(a)   #['car', 'bus', 'bike', 1, 2, 3, ['Value1', 1, 2, 3, 'Value2'], [['1', 2, 3, 'Helloworld'], '2', '3', 'Hello'], [4, 3, 2, 1, 2, 3]]

#List Extention
bike=['TVS', 'Apache', 'ScootyPep']
cars = ['a','b','c','d','A','C','B'] 

cars.extend(bike)
print(cars)  #['a', 'b', 'c', 'd', 'A', 'C', 'B', 'TVS', 'Apache', 'ScootyPep']
print(bike) #['TVS', 'Apache', 'ScootyPep']

#List copy
mylist = cars.copy()
print(mylist)  #['a', 'b', 'c', 'd', 'A', 'C', 'B', 'TVS', 'Apache', 'ScootyPep']

mylist2=list(cars)
print(mylist2) #['a', 'b', 'c', 'd', 'A', 'C', 'B', 'TVS', 'Apache', 'ScootyPep']

#List concatenate
car_model=["Audi","Toyota"]  #creating a new list for concatenating

mylist3 = cars+car_model
print(cars+car_model) #['a', 'b', 'c', 'd', 'A', 'C', 'B', 'TVS', 'Apache', 'ScootyPep', 'Audi', 'Toyota']
print(mylist3) #['a', 'b', 'c', 'd', 'A', 'C', 'B', 'TVS', 'Apache', 'ScootyPep', 'Audi', 'Toyota']

#List Remove Vs Delete
cars = ['a','b','c','BMW','BMW','C','B'] 
cars.remove('BMW')
print(cars)  #['a', 'b', 'c', 'BMW', 'C', 'B']

#cars = ['a', 'b', 'c', 'BMW', 'BMW', 'C', 'B']

#cars = [car for car in cars if car != 'BMW']
#print(cars)



#Nested List
nested = [cars,cars]
print(nested)

#Slice a list
print(cars[0:2])
print(cars)

print(cars[0:])
print(cars)

print(cars[:-3])
print(cars)



#Update an value on the list
cars = [1,'a','b','c','Volvo',12.50]
cars[1] = 'Volvo'
cars[0] = 'VOLVO'  #['VOLVO', 'Volvo', 'b', 'c', 'Volvo', 12.5]

print(cars)

#Updating multiple value on the list
cars[0:2] = ['vOLVO','vOLVO','Volvo'] #['vOLVO', 'vOLVO', 'Volvo', 'b', 'c', 'Volvo', 12.5]
cars[0:3] = ['vOLVO','vOLVO','Volvo'] #['vOLVO', 'vOLVO', 'Volvo', 'c', 'Volvo', 12.5]
print(cars)  


'''

'''
#Stacks and Queue
#The list methods make it very easy to use a list as a stack or queue.
#A stack is a data structure (though not available directly in Python) where the last
#element added is the first element retrieved, also known as Last In, First Out (LIFO).
#A list can be used as a stack using the append() and pop() method.
# (Bottom) 1 -> 5 -> 6 (Top)
stack = [1, 5, 6]

stack.append(4) # 4 is added on top of 6 (Top)
stack.append(5) # 5 is added on top of 4 (Top)

print(stack) #[1, 5, 6, 4, 5]

stack.pop() #
stack.pop() #
stack.pop() #

print(stack)

stack.append([5])
print(stack)

Queue:
The first element added is the first element retrieved, also known as First In, First Out (FIFO). 
Consider a queue at a ticket counter where people are catered according to their arrival sequence 
and hence the first person to arrive is also the first to leave.

In order to implement a queue, we need to use the collections.deque module; 
It can be created using the append() and popleft() methods.

#Import 'deque' module from the 'collections' package
from collections import deque

# Define initial queue
queue = deque(['Perl', 'PHP', 'Go'])
queue.append('R')
print(queue)

# 'Python' arrives and joins the queue
print(queue.append('Python'))

# The first to arrive leaves the queue
queue.popleft()
print(queue)


#Tuples
#Tuples are similar to lists — they allow you to display an ordered sequence of elements. 
#However, they are immutable and you can’t change the values stored in a tuple. 
#The advantage of using tuples over lists is that the former are slightly faster. 
#So it’s a nice way to optimize your code.

#Tuples are Ordered / Index based / Duplicate / Static*
#Tuples allows duplicate. It allows all data types. 
#Tuple syntax - ()

cars = ('BMW','VOLVO',12,12.5,True)

#cars.pop()  #'tuple' object has no attribute 'pop'
#Tuple Length
print(len(cars)) #5

#Tuple Index
print(cars.index('BMW')) #0

#Tuple Count
print(cars.count('TRUE')) #0
print(cars.count('Techiesmiles')) #0
#print(cars.index('TechieSmiles')) #ValueError: tuple.index(x): x not in tuple

#Updating a value in Tuple
cars = ('bmw','volvo')
print(type(cars)) #Tuple

Y=list(cars) 
print(type(Y)) #List

Y[0] = 'BMW'

Y.append('value1') #BMW, volvo, value1

Y[1]=['Value2','Value3','Value4']
print(Y)
print(type(Y)) 

cars=tuple(Y)
print(type(cars)) #tuple #('BMW', ['Value2', 'Value3', 'Value4'], 'value1')
print(cars)

print(cars[1][1]) #Value3
print(cars[0]) #BMW




#SET
#SET is Unordered / Unindexed.
#SET will not allow any duplicate values. It is Mutable.
#It will allow all data types.
#Set Syntax {} or set() function

cars = {'bmw', 'ford', 'Toyota', 'BMW', 'bmw',12,12.5,True}

print(type(cars)) #<class 'set'>

#SET Length
print(len(cars)) #7
#print(cars.count('bmw'))

#SET Add
cars.add('TOYOTA')
print(cars) #{True, 'TOYOTA', 'BMW', 'bmw', 12, 12.5, 'Toyota', 'ford'}

cars.add('bmw')
print(cars) #{True, 'TOYOTA', 'BMW', 'bmw', 12, 12.5, 'Toyota', 'ford'}

#SET Remove
cars.remove('bmw') #{True, 'TOYOTA', 'BMW', 12, 12.5, 'Toyota', 'ford'}
print(cars)

#cars.remove('bmw')
#print(cars) #KeyError: 'bmw'  - It will allow the program to proceed further. 

#SET Discard
cars.discard('bmw')
print(cars) #It will remove the value if present, otherwise it will by-pass the program to proceed with next step.

#SET Delete
#del(cars)

cars.pop()
print(cars) #{True, 'ford', 12, 12.5, 'BMW', 'TOYOTA'} - Pop will remove the first value from the set
print(cars.pop()) #True
print(cars) #{12, 12.5, 'TOYOTA', 'ford', 'BMW'}

#cars.pop(3)
#print(cars) #TypeError: pop() takes no arguments (1 given) - Pop takes no argument in SET 

#cars.insert(2,'volvo') 
#print(cars) #'set' object has no attribute 'insert'

cars.add('Volvo') #TypeError: add() takes exactly one argument (2 given)
print(cars)

#SET Pop, clear


#Dictionary
#Dictionary is Unordered / Key and Value pair. #{key:value}
#A dictionary holds indexes with keys that are mapped to certain values. 
#These key-value pairs offer a great way of organizing and storing data in Python. 
#They are mutable, meaning you can change the stored information. 
#A key value can be either a string, Boolean, float or integer. Here’s an example dictionary illustrating this:

#Example:  A dictionary is like a phone-book where we can find the phone numbers or contact details of a person by knowing only his/her name 
#i.e. we associate names (keys) with corresponding details (values).
#Note that the keys must be unique just like the way it is in a phone book i.e. we cannot have two persons with the exact same name.

#Syntax
#dictionary = {key1 : value1, key2 : value2, key3 : value3}

#How to create a Dictionary
#Option 1: dict = {Key:value}
#Option 2: dict = (name:value)

new_dict = {'brand':'Honda', 
            'model': 'Civic', 
            'year': 1995}

print(new_dict) #{'brand': 'Honda', 'model': 'Civic', 'year': 1995}
print(type(new_dict)) #<class 'dict'>

#Create Dict with multiple DataTypes

ticker = {'symbol' : 'AAPL',
'price' : 224.95,
'company' : 'Apple Inc',
'founded' : 1976,
'products' : ('Machintosh', 'iPod',
'iPhone', 'iPad')}

print(type(ticker)) #<class 'dict'>

#How to get values from the dictionary based on the Key

print(ticker['company'])
print(ticker['products'][1])

print(ticker['products'][2]) #['iPad']
print(ticker['company']) #'Apple Inc'
#print(ticker.get('company')) 'Apple Inc'

#How to add values in the list under Dictionary?

#ticker['products']='Iphone12'
#ticker['products'][1,'Iphone14'] #TypeError: string indices must be integers
newvalue = 'Iphone12'
ticker['products'].append[('Apple Watch')] # Check
print(ticker)


#What is Nested Dictionary?
#We can also provide a dictionary as a value to another dictionary key. Such a dictionary is called nested dictionary. 
#Take a look at below example:

tickers = {'AAPL' : {'name' : {'price':234},'price' : 224.95},
           'GOOG' : {'name' : 'Alphabet Inc.','price' : 1194.64}}

print(tickers) #{'AAPL': {'name': 'Apple Inc.', 'price': 224.95}, 'GOOG': {'name': 'Alphabet Inc.', 'price': 1194.64}}

print(tickers['AAPL']) #
print(tickers['AAPL']['name']['price']) #
#tickers['AAPL']['Location':'America']
print(tickers)


#Assigning same name to multiple values in Dict
demo = {'cars':'Jaguar', 'cars':'Jaguar2'}
print(demo)
#In the above example, Python discarded the value cars and retained the latest value assigned to the same key.

#Altering Dictionaries
#A value in a dictionary can be updated by assigning a new value to its corresponding key using the assignment operator =.

ticker = {'symbol' : 'AAPL',
'price' : 224.95,
'company' : 'Apple Inc',
'founded' : 1976,
'products' : ['Machintosh', 'iPod',
'iPhone', 'iPad']}

ticker['products']= ['Iphone12']
print(ticker)
#How to add a new value in the dictinoary?
ticker['products'].append('iphone14')
print(ticker)

#How to insert a new key value pair
my_dict = {"key1": "value1", "key2": "value2"}
new_key = "key3"
new_value = "value3"
my_dict[new_key] = new_value
print(my_dict)  #{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

my_dict['key4'] = ['Value4']
print(my_dict) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': ['Value4']}

#How to insert a new key value pair at a particular index position
#Dictionaries in most programming languages are inherently unordered collections, which means they don't have index positions like lists or arrays. 
#Therefore, you can't directly insert a new key-value pair at a specific index position in a dictionary.
#However, if you want to maintain a specific order for your key-value pairs, you can use an ordered data structure like a list of tuples or a special ordered dictionary

# Using a list of tuples to maintain order
ordered_dict = [("key1", "value1"), ("key2", "value2")]

# Insert a new key-value pair at a specific index
new_index = 1
new_key = "key3"
new_value = "value3"
ordered_dict.insert(new_index, (new_key, new_value))
print(ordered_dict)

ordered_dict.insert(1,('new4', 'value5'))
print(ordered_dict)

a = {'Key1':'Value1','Key2':'Value2','Key3':'Value3'}
print(a['Key1'])

ticker = {'symbol' : 'AAPL',
'price' : 224.95,
'company' : 'Apple Inc',
'founded' : 1976,
'products' : ['Machintosh', 'iPod',
'iPhone', 'iPad']}

#Adding a new values
ticker['products'].append(['Walkman','Airpod','Headset'])
print(ticker)
#{'symbol': 'AAPL', 'price': 224.95, 'company': 'Apple Inc', 'founded': 1976, 
# 'products': ['Machintosh', 'iPod', 'iPhone', 'iPad', ['Walkman', 'Airpod', 'Headset']]}

#Updating an existing value
ticker['products']=['Walkman','Headsets','Airpod']
print(ticker)
#{'symbol': 'AAPL', 'price': 224.95, 'company': 'Apple Inc', 'founded': 1976, 'products': ['Walkman', 'Headsets', 'Airpod']}
'''

ticker = {'Key1':'Value1', 'Key2': 'Value2'}
#Dictionary Items
#items() : This method returns a object containing all times in the calling object.
print(ticker.items())
#dict_items([('symbol', 'AAPL'), ('price', 224.95), ('company', 'Apple Inc'), ('founded', 1976), ('products', ['Walkman', 'Headsets', 'Airpod'])]) 

#Dictionary Keys
#keys() : This method returns all keys in the calling dictionary
print(ticker.keys())
# dict_keys(['symbol', 'price', 'company', 'founded', 'products'])

#Dictionary Values
#values() : This method returns all values in the calling object.
print(ticker.values())
#dict_values(['AAPL', 224.95, 'Apple Inc', 1976, ['Walkman', 'Headsets', 'Airpod']])

#Copying values from a Dictionary to new dictionary
#As the name suggests, this method copies the calling dictionary to another dictionary.
newticker = ticker.copy()
print(newticker)

#pop
#This method pops the item whose key is given as an argument.
print(newticker.pop('Key1')) 
#TypeError: pop expected at least 1 arguments, got 0 - In Dictionary, we have to pass the key detail, otherwise it will throw error.
print(newticker)

#In pop - Key details should be passed as a input argument, value should not be considered

