# Other Important Topics

# Namespace and Scope
'''
Namespace and scope are fundamental concepts in Python that define how variables and names are organized and accessed in a program:

Namespace:
A namespace is a container that holds a collection of identifiers (such as variable names, function names, class names, etc.) and their corresponding objects (values or functions).
It acts as a mapping from names to objects, allowing you to uniquely identify and access these objects.
In Python, namespaces are organized hierarchically, forming a tree-like structure. 
The most common namespaces include the built-in namespace, global namespace, and local namespaces associated with functions and classes.

Scope:
Scope defines the region or context in which a name (variable, function, etc.) is accessible and can be used in a Python program.
(or) A scope is the region in your program where certain identifiers are visible or accessible.

Python uses two scopes:
Local scope: The local scope represents variables that are defined within a function but outside any nested block. 
Global scope: The global scope represents all other variables (including those declared at module level).

x = 10  # Global scope

def foo():
    y = 5  # Local scope
    print(x)  # Accesses the global 'x'

def bar():
    x = 20  # Local scope (different from the global 'x')
    print(x)  # Accesses the local 'x'

foo()  # Prints 10
bar()  # Prints 20


Built-in scope: This is the highest level of scope and contains names of built-in functions 
and objects like print(), len(), and str().

'''

# DocStrings (Documentation Strings)
'''
A docstring in Python is a specially formatted string used to document functions, classes, or modules, 
providing information about their purpose, usage, and behavior for better code understanding and automated documentation generation. 
It is typically placed as the first statement inside a definition and follows specific conventions outlined in PEP 257.

def add(x, y):
    """
    This function takes two numbers as input and returns their sum.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.

    """
    return x + y

print(add.__doc__) 
print(add(1,2))

'''
# Pow

'''
In Python, the pow() function is used to calculate the power of a number. 
It takes two arguments: the base number and the exponent, and returns the result of raising the base to the power of the exponent.

Syntax:
pow(base, exponent, modulus)

# Calculate 2^3
result = pow(2, 3)
print(result)  # Output: 8

# Calculate (2^3) % 5
result = pow(2, 3, 5)
print(result)  # Output: 3

'''
# Calculate 2^3
result = pow(2, 5)
print(result)  # Output: 8

a = []
for i in range(2,3):
    a.append(i**5)
    print(a)

