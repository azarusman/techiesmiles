#Python OOPS
'''
#OOPS:

Object-Oriented Programming is a programming paradigm that revolves around the concept of objects, which are instances of classes. 
OOP helps you organize your code into more manageable and reusable structures. 
Python is an object-oriented programming language, and it fully supports the creation and usage of classes and objects.

Object              -- Instance of Class
Class               -- Blue print of Object
Encapsulation       -- Protecting our data
Polymorphism        -- Different behaviors at differenct instances
Abstraction         -- Hiding our irrelevant Data
Inheritance         -- Extending the properties of a class to another class.

#Classes and Objects:
A class is a collection of objects. 
A class is a blueprint for creating objects. It defines attributes (variables) and 
methods (functions) that the objects will have.

Object
An instance of a class. It has its own behavior and identity.

Class: A blueprint or architectural plan for a house.
Object: An actual house built according to the blueprint, with windows, cupboards, furniture, and other elements.

#Attributes and Methods:
Attributes are variables that hold data specific to a class or object.
Methods are functions defined within a class that operate on its data.

#Encapsulation:
Encapsulation is the practice of hiding the internal details of an object and exposing only what's necessary for its interaction.
This is achieved by marking attributes and methods as private (using a single underscore) or very private (using a double underscore).

#Inheritance:
Inheritance allows a class (subclass or derived class) to inherit attributes and methods from another class (base class or parent class).
It enables code reuse and promotes the creation of specialized classes.

#Polymorphism:
Polymorphism allows objects of different classes to be treated as objects of a common superclass.
This enables code to work with objects at a higher level of abstraction, without being concerned about their specific types.

#Method Overriding:
Subclasses can provide a different implementation of a method that is already defined in a parent class. 
This is known as method overriding.

#Constructor and Destructor:
The constructor (__init__ method) initializes the attributes of an object when it is created.
The destructor (__del__ method) is responsible for cleaning up resources when an object is no longer needed.

#Class Variables vs. Instance Variables:
Class variables are shared among all instances of a class and are defined outside of methods.
Instance variables are unique to each instance of a class and are typically defined within the constructor.

#Example
# Defining a class named 'car'

class Car:
    # Class attribute
    Name = 'BMW'        
    Model = 2019
    print(Name +' ' + str(Model))  # This will print 'BMW 2019'        

    # Method of the class
    def func1(self):
        a = 10    # Local variables (a,b,c) - Inside the method
        b = 20
        c = a + b 
        print(c)

    # Another method of the class
    def func2(self):
        print("Hello")

# Creating an object of the 'Car' class
c1 = Car()

# Calling the 'func1' method of the object
c1.func1()  # This will print the result of the calculation and 'None' (as the method doesn't return a value)

# Calling the 'func2' method of the object
c1.func2()  # This will print "Hello"

#Python Constructor or Special Method
A constructor is a special method that gets called when an object of a class is created. 
It is used to initialize the attributes (properties) of the object. 

There are 2 types of Constructor:

1. Default Constructor
2. Parameterized Constructor 

__init__(self) - #Syntax

#Default Constructor
# Define a class named School
class School:

    # Constructor method (__init__)
    def __init__(self):
        # Instance variables initialized within the constructor
        self.StudentName = 'TechieSmiles'  # Instance Variable representing student name
        self.Section = 'B'  # Instance Variable representing section
        print("I'm calling the Default Constructor")

    # Method to display student details
    def details(self):
        print("My name is", self.StudentName)
        print("I belong to section", self.Section)
        print("I'm coming from the method")

# Creating an object (instance) of the School class
a1 = School()

# Calling the 'details' method of the object
a1.details()

#Parameter Constructor

# Define a class named School
class School:

    # Parameterized constructor method (__init__)
    def __init__(self, StudentName, Section):
        # Instance variables initialized with values from constructor parameters
        self.StudentName = StudentName  # Instance Variable representing student name
        self.Section = Section  # Instance Variable representing section
        print("I'm calling the Parameter Constructor")

    # Method to display student details
    def details(self):
        print("My name is", self.StudentName)
        print("I belong to section", self.Section)
        print("I'm coming from the method")

# Creating an object (instance) of the School class with constructor parameters
a1 = School('Techie', 'B')

# Calling the 'details' method of the object
a1.details()

#Encapsulation

class MyClass:
    def __init__(self):
        self._protected_attribute = "Hello, protected!"

    def dummy(self):
        return self._protected_attribute

# Creating an instance of MyClass
obj = MyClass()
print(obj.dummy())

# Accessing the protected attribute directly (not recommended)
print(obj._protected_attribute)  # This works, but it's against the naming convention

# Modifying the protected attribute directly (not recommended)
obj._protected_attribute = "Modified!"
print(obj._protected_attribute)  # This works as well


class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Using a single underscore for protected attribute
        self._balance = balance  # Using a single underscore for protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

# Creating a BankAccount instance
account = BankAccount("123456789", 1000)

# Accessing attributes using methods
print("Account Number:", account.get_account_number())
print("Initial Balance:", account.get_balance())

# Making deposits and withdrawals
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)

# Accessing attributes directly (not recommended due to encapsulation)
print("Current Balance:", account._balance)

#Polymorphism - Method Overriding

Using same method in Parent and Child and trying to call with the same name. 
It allows objects of different classes to be treated as objects of a common superclass.

There are two main types of polymorphism in Python: 
1. Compile-time (or static) polymorphism
2. Runtime (or dynamic) polymorphism. 

#Compile-Time Polymorphism (Method Overloading):
This involves defining multiple methods in a class with the same name but different parameter lists. 
The appropriate method to be executed is determined by the number or type of arguments passed during the function call.

#Runtime Polymorphism (Method Overriding):
This occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. 
The overridden method in the subclass has the same name and parameters as the one in the superclass. 
When you call the method on an object of the subclass, the overridden method in the subclass is executed instead of the method in the superclass.

#Example of Method Overloading

class Calculator:
    def add(self, a, b=None):
        if b is None:
            return a
        return a + b

calc = Calculator()

print(calc.add(5))      # Output: 5 (only 'a' provided)
print(calc.add(5, 3))   # Output: 8 (both 'a' and 'b' provided)

# From the above, 'add' method in the 'Calculator' class is overloaded to accept either one or two aruguments.
# If only one argument is provided, it assumes the second argument is None and returns the value of the first argument.
# If two arguments are provided, it performs the addition.

#Example of Method Overriding

class School:
    
    def Section(self):
        pass

class Biology(School):

    def Section(self):
        SectionA = '42 Students'
        return SectionA
    
class Maths(School):

    def Section(self):
        SectionA = '45 Student'
        return SectionA
    
def strength(School):
    return School.Section()

Bio = Biology()
Mat = Maths()

print(strength(Mat))

#Inheritance
Extending the properties of a class to another class.
It's a way to create a new class that inherits attributes and behaviors (methods) from an existing class.

#Employee details 

class Employee:
    name = 'Raj'            #Parent variable
    
    def __init__(self):     #Parent Constructor
        print("I'm a parent") 

    def empdetails(self):       #Parent method
        print('Helloworld_1')

class Developer(Employee):  #Derived class
    name = 'Kumar'          #Child variable

    def __init__(self):     #Child contructor
        super().__init__()  #Super Keyword calling Parent Constructor
        print(super().name) #Super keyword calling Parent Variable
        print('Helloworld_2')

    def dept(self):         #Child method
        print('Helloworld_3')

    def HR_Dept(self):          #child method
        super().empdetails()    #Super keyword Calling the Parent method
        print('Helloworld_4')

D1 = Developer()

#Super Keyword -- super()

1. If a Constructor (__init__) is present in parent, then the parent constructor will execute. 
2. If a Constructor is present in child & Parent class then the child will execute. Note: Parent constructor will not execute. 

To call both Parent & Child constructor present in a block of code, we should use Super() keyword: Super().__init__()
To call the Parent variable, then we have to use the super keyword as mentioned: super().name

Super Keyword Syntaxes:
super().__init__()  --> To call the Parent Constructor
super().Method()    --> To call the Parent Method
super().variable()  --> To call the Parent variable

'''