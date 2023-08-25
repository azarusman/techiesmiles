#Python Functions
'''
A function is a block of code(that performs a specific task) which runs only when it is called. 
Functions are essential for organizing and structuring code, making it more readable, modular, and maintainable.

There are three types of functions in Python:

• Built-in functions such as print to print on the standard output device, type to check data type of an object, etc. 
  These are the functions that Python provides to accomplish common tasks.
• User-Defined functions: As the name suggests these are custom functions to help/resolve/achieve a particular task.
• Anonymous functions, also known as lambda functions are custommade without having any name identifier.

'''

# User-Defined Function:
'''
#syntax

def <function_name>():

    //Block of code
    //Block of code

<function_name()>

#1st program

def my_func():

    print("Helloworld")

my_func()  #User has called this function

#2nd Program using Parameters

def sum(a=6,b=7):
    z = a+b
    print(z)

sum()
#Note: We can pass a fixed value to the parameter

#3rd Program using Parameters by passing runtime parameter value
def sum(a,b):
    z = a+b
    return z
print(sum(2,0))

#Note: We can pass the value to the parameters runtime. 


#4th Program by passing overwritting the parameter value
def sum(a=6,b=7):
    z = a+b
    print(z)

sum(b=5)

def sum(a=6,b=7):
    z = a+b
    print(z)

sum(9)

#Note: We have already passed values for both the parameters, but the user has passed the value while calling the function. 
       #so latest values will be considered, old values will be overwriten by new values. 

#5 Assigning a default value to the parameter


def my_func1(name,age):
    print(name,' ', age)

my_func1('Saran')


def my_func1(name,age=20):
    print(name,' ', age)

my_func1('Azar',30)

def my_func1(name,age=20):
    print(name,' ', age)

my_func1('Azar',30)

#We cannot set the left parameter as a static and right parameter as dynamic. It will throw syntax error as 'non-default argument follows default argument'

#def my_func1(name='Techiesmiles',age):
 #   print(name, ' ', age)

#my_func1(age=20)


#my_func1(30)
#SyntaxError: non-default argument follows default argument

#What is Return?
#Return will help to store the value and return it when the function is called. 
#Return is majorly used to pass the stored value outside of the program. 

def my_func1 (Tam, Eng):
    total=Tam + Eng

    return total

total = my_func1(35,35)

print(total)

# From the above program, 
# Tam + Eng summed value is stored in the total 
# return will store the value and pass it wherever the 'total' is called.

#*args & **kwargs

#The `*args` parameter is used to accept 'n' number of arguments from the user dynamically.
#The '**args' parameter is used to accept 'n' number of dict arguments from the user dynamically.

def my_func2(*args):
    result = 0
    for i in args:
        result+=i

    return result

print(my_func2(10,12,3,4,5))


def my_func3(**kwargs):
    for key, value in kwargs.items():
        print(key + ':' + value )

print(my_func3(Company='Apple', Location='America'))

#Local and Global Variables

#Local Variables - Calling inside a function
#Global Variables - Can be used In/Outside of the function. 

#Local Variables
def my_func():
    a = 10
    b = 20
    
    c = a + b

    print(c)

my_func()

#In the above function, we can see that all 3 variables (a,b,c) is mentioned inside the function and it is called through the function. 

#Global Variables

a = 20

def my_func1():

    b = 20
    c = a + b

    print(c)

my_func1()

#In the above function, we can see that 1 variable (a) mentioned outside of the function. 
#Remaining 2 variables (b,c) is mentioned inside the function. 
#All 3 variables are used in the function. So, here (a) is referred as Global Variable. 

a = 20

def my_func3():
  
    global a
    print("This value is " + str(a)) # 20

    a = 5

    print("This value is "+ str(a)) # 5 
    print('this value is '+ str(a)) # 5

my_func3()

print('this value of a is ' + str(a)) # 5 #20


a = 20

def my_func3():
    global a
    #global keyword makes it possible to access and modify the variable declared globally.
    print("This value is " + str(a))

    a = 5

    print("This value is "+ str(a))
    print('this value is '+ str(a))

my_func3()

print('this value of a is ' + str(a))

#Palindrome Program - 

str1 = input('Enter your input ').lower()
str2 = ''
index = -1

for i in str1:
    str2+=str1[index]
    index-=1

print(f'The given string is {str1} \nThe revered string is {str2}')

if str2==str1:
    print(f'Given value is a Palindrome {str1}')

else:
    print('Given word is not a palindrome')


# Palindrom in function
def palindrome():

    str1 = input('Enter your input ').lower()

    str2 = ''
    index = -1

    for i in str1:
        str2+=str1[index]
        index-=1

    print(f'The given string is {str1} \nThe revered string is {str2}')

    if str2==str1:
        print(f'Given value is a Palindrome {str1}')

    else:
        print('Given word is not a palindrome')

palindrome()
'''
double = lambda x: x ** 2
print(double(5))

