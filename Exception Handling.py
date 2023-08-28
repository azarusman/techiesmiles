#Exception Handling
'''
Exception handling is a crucial aspect of programming that helps you deal with unexpected situations and errors in code.

Errors are problems in a program due to which the program will stop the execution.
Exceptions are raised when some internal events occur which change the normal flow of the program. 

Types of Exception in Python:

SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, 
            such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.

'''
'''
#Syntax Error
# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if(amount > 2999)
    print("You are eligible to purchase Dsa Self Paced") #SyntaxError: invalid syntax

#Type Error

x = 5
y = "hello"
z = x + y # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'

#NameError
class a:
    b = 10
    c = 20
    d = b + c
    print(e)

c1 = a()
print(c1) #NameError: name 'e' is not defined

#IndexError
a=[1,2,3,4,5]
print(a[6]) #IndexError: list index out of range

#KeyError
a = {'Location':'America','Salary':123, 'Dept':'IT'}
print(a['JoiningDate']) #KeyError: 'JoiningDate'

#ValueError
a =int(input('Enter your age '))
print(a) #ValueError: invalid literal for int() with base 10: 'TechieSmiles'


#ZeroDivisionError
# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a) #ZeroDivisionError: division by zero

#AttributeError

class cars:
    def __init__(self, value):
        self.value = value

cars1 = cars('BMW')
print(cars1.value1) #AttributeError: 'cars' object has no attribute 'value1'

#FilenotFoundError or I/OError

filepath = 'C:\\Users\\Elait141\\Desktop\\Techie Smiles\\Python\\Files\\Python File.txt'
with open(filepath,'r') as f:
    t = f.read()
    print(t)  #FileNotFoundError: [Errno 2] No such file or directory: ''

#How to handled this exception and error in python?

# try, except and finally block
# try and except for FilenotFoundError handling

filepath = 'C:\\Users\\Elait141\\Desktop\\Techie Smiles\\Python\\Files\\PythoFile.txt'

try:
    with open(filepath,'r') as f:
        t = f.readlines()
        print(t)

except FileNotFoundError:
    print('File not found')

#try and except for TypeError handling
x = 5
y = "hello"

try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")
        
#try, except for exception handling
# Program to depict else clause with try-except
# Function which returns a/b
def myfunc(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
myfunc(2.0, 3.0)
myfunc(3.0, 3.0)

# Python program to demonstrate finally
# No exception Exception raised in try block
try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')

# Program to depict Raising Exception
In Python, the `raise` statement is used to raise an exception manually. 
This means you can intentionally trigger an exception under specific conditions within your code. 
The `raise` statement allows you to create and raise custom exceptions or trigger built-in exceptions when certain conditions are met.

'''




