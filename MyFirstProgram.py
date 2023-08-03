
'''
#FirstProgram
print('Helloworld')
print('Helloworld!!!')
print('Helloworld@123')
print('Helloworld@1!')

msg = 'HelloWorld!'
print(msg)   # Output: HelloWorld!


#What is a Variable?
#1. A variable can be thought of as a container having a name which is used to store a value. 
#2. In programming parlance, it is a reserved memory location to store values. 

#Sum of two number
#Method 1:
print(10+20+30)

#Method 2:
a = 10
b = 20
c = a+b

print(c)
print('sum of a + b is ', c)



#Subraction of two numbers
#Method 1:
print(10-20) #Output = -10

#Method 2:
a=10
b=20
c=a-b 
print (c) #Output = -10
print ('Subraction of a, b is ', c) #Output = Subraction of a, b is -10


#Multiplication of two numbers
#Method 1:
print(10*20) #Output = 200

#Method 2:
a = 10
b = 20
e = (a*b)
print('Multiplication of a and b is ', e) #Output - Multiplication of a and b is 200

#Division of two numbers

#Method 1:
print(10/20) #Output: 0.5

#Method 2:
a=10
b=20
f = a/b
print('Division of a, b is ', f) #Output: Division of a, b is 0.5


#Modulus

#Method 1:
print(10%20) #Output: 10

#Method 2:
a= 30
b= 20
g = a%b
print('Reminder when dividing of a and b is ', g) #Output: Reminder when dividing of a and b is 10

#Integer Division Operator

a = 5
b = 3
h = a // b
print(h) #Output = 1

#Concatenating string and integer literal

print("January", 2010) #Output: January 2010
print('January', 2010) #Output: January 2010
print("I bought few car's in January", 2020) #Output: I bought few car's in January 2020
print('I bought few car"s in January', 2020) #Output: I bought few car"s in January 2020


#Concatenating two strings

#'Today is 1st day of class'
#'We are learning Python'

print ('Today is 1st day of class' + 'We are learning Python') 
#Output: Today is 1st day of classWe are learning Python

print ('Today is 1st day of class. ' + 'We are learning Python')
#Output: Today is 1st day of class. We are learning Python

print ('Today is 1st day of class.' + ' ' + 'We are learning Python')
#Output: Today is 1st day of class. We are learning Python

print('I bought few car\'s on January') #Output: I bought few car's on January
print("I bought few car\"s on January") #Output: I bought few car"s on January

print("I bought few \"cars\" on January") #Output: I bought few "cars" on January


#Concatenating a variable and string values

Msg1 = "Today is 1st day of class"
#"We are learning Python"
print (Msg1 + "We are learning Python") #Output: Today is 1st day of classWe are learning Python

#Formating the string

Msg1 = "In our day 1 class"
#"We are learning Python"

print("We are learning Python," + Msg1)    #Output: We are learning Python,In our day 1 class
print("We are learning Python,", Msg1)     #Output: We are learning Python, In our day 1 class
print(f"We are learning Python, {Msg1}")  #Output: We are learning Python, In our day 1 class


Msg1 = "In our day 1 class"
Msg2 = 'Total no. of students is'
Msg3 = 6

print(Msg1,'we are learning Python', Msg2, Msg3)
#Output: In our day 1 class we are learning Python Total no. of students is 6

print(f"{Msg1} we are learning Python {Msg2}{Msg3}")
#Output: In our day 1 class we are learning Python Total no. of students is6


#Format Function
Msg1 = "In our day 1 class"
Msg2 = 'total no. of students is'
Msg3 = 6

print ('we are {x}, currently we have {y} {z} '.format(x=Msg1, y=Msg2, z=Msg3))
#Output: we are In our day 1 class, currently we have total no. of students is 6 

Msg1 = "In our day 1 class"
Msg2 = 'total no. of students is'
Msg3 = 6

print ('we are {0}, currently we have {1} {2} '.format(Msg1, Msg2, Msg3))
#Output: we are In our day 1 class, currently we have total no. of students is 6 

#Multiple Variable assignment

intvar , floatvar , strvar = 10,2.57,"Python Language"

print(intvar, floatvar, strvar) #Output: 10 2.57 Python Language

p1 = p2 = p3 = p4 = 44
print(p1,p2,p3,p4) #Output: 44 44 44 44


#Escape Sequence

#Escape characters are generally used to perform certain tasks and their
#usage in code directs the compiler to take a suitable action mapped to that
#character.

print(" That's really easy.")
print('That\'s really easy.') #That's really easy.

#Newline
print('That is really easy. Yes, it really is.')
print('That is really easy.\n Yes, it really is.')
#Output: 
# That is really easy.
 #Yes, it really is.

#Tab
print('SQL \t "Manual Testing" \t Python')
#Output: SQL      "Manual Testing"        Python

#No new line added
print('TS is the Short word for TechieSmiles.\
 It is a technology company.')  

#Output: TS is the Short word for TechieSmiles. It is a technology company.


#Indentation Error (Spaces between codes)
#1. Whitespaces are important in Python. Whitespace at the start of a line is called indentation. 
#2. It is used to mark the start of a new code block. 
# A block or code block is a group of statements in a program or a script. 
#3. Leading spaces at the beginning of a line are used to determine the indentation level, 
# which in turn is used to determine the grouping of statements. Also, statements which go together must have same indentation level.

#Msg1 = 'This is a sample of Identation Error'
#print(Msg1)


a= 10
b = 20
c = 20
_c = 20
*c =20
_1 = 20

#Variable Naming Conventions
A variable can have a short name or more descriptive name.

Rules to create a variable
1. A variable name must start with a letter or the underscore character.
stock = 'AAPL' # Valid name
_name = 'AAPL' # Valid name

2. A variable name cannot start with a number.
1stock = 'AAPL' # Invalid name
1_stock = 'AAPL' # Invalid name

3. A variable name can only contain alpha-numeric characters(A-Z, a-z, 0-9) and underscores( _ ).
# Valid name. It starts with a capital letter.
Stock = 'AAPL'

# Valid name. It is a combination of alphabets and the underscore.
stock_price = 226.41

# Valid name. It is a combination of alphabets and a number.
stock_1 = 'AAPL'

# Valid name. It is a combination of a capital letter, alphabets and a number.
Stock_name_2 = 'MSFT'


4. A variable name cannot contain whitespace and signs such as +, -, etc.
# Invalid name. It cannot contain the whitespace.
stock name = 'AAPL'

# Invalid name. It cannot contain characters other than the underscore(_).
stock-name = 'AAPL'

5. Variable names are case-sensitive.
# STOCK, stock and Stock all three are different variable names.
STOCK = 'AAPL'
stock = 'MSFT'
Stock = 'GOOG'

6. Python keywords cannot be used as a variable name.
# 'str', 'is', and 'for' CANNOT be used as the variable name as they are reserved keywords in Python. Below given names are invalid.
str = 'AAPL'
is = 'A Variable'
for = 'Dummy Variable'

#The following points are  practices followed by professional programmers.
#Use a name that describes the purpose, instead of using dummy names. In other words, it should be meaningful.
# Valid name but the variable does not describe the purpose.
a = 18

# Valid name which describes it suitably
age = 18

#Use an underscore character _ to separate two words.
stockname = 'AAPL' # Valid name.

And it also provides concise readability.
stock_name = 'AAPL' # Valid name. 

# Start a variable name with a small alphabet letter.
Stock_name = 'AAPL' # Valid name.

#Additionally, it refers to uniformity with other statements.
stock_name = 'AAPL' # Valid name. 

#DataTypes

#Python has four basic data types:
1. Integer
2. Float
3. String
4. Boolean


#Integer
#An integer can be thought of as a numeric value without any decimal. In fact, it is used to describe any whole number in Python such as 7, 256, 1024,
#etc.

stock_price = 224
print(stock_price)
print(type(stock_price))

#Float
#A float stands for floating point number which essentially means a number with fractional parts. 
#It can also be used for rational numbers, usually ending with a decimal such as 6.5, 100.1, 123.45, etc

stock_price = 224.61
print(stock_price)
print(type(stock_price))

c = 'TechieSmiles'
d = '123'
print(type(c))
print(type(d))
print(c+d)

## From the statistics perspective, a float value can be thought of as a continuous value, whereas an integer value can
#correspondingly be a discrete value
x = 2
y = 10.0

print(x + y)
print(x - y)
print(x * y)
print(x / y)

#String
#A string is a collection of alphabets, numbers, and other characters written within a single quote ' or 
#double quotes ". In other words, it is a sequence of characters within quotes.

#Variable assignment with a string
sample_string = '1 can also be expressed as 0.01%'  #check
print(sample_string)

stock_price = '224.61'
print(sample_string)
print('Price of AAPL is ' + stock_price)

stock_price = 224.61
print(sample_string)
print('Price of AAPL is ' + stock_price)

#String Multiplication
Sample_string = 'Python! '
print(Sample_string)

print(Sample_string * 10)

#String Slicing
#Slicing is performed using the square brackets []. The syntax for slicing a single element from the string is [index] which will return an element at index.
#The index refers to the position of each element in a string and it begins with 0, which keeps on increasing in chronological order for every next element.

string = 'EPAT Handbook!'
string1 =123

print(string[0]) # 0 refers to an element E
print(string[1]) # 1 refers to an element P
print(string[0:3]) # 3 refers to an element EPAT
print(string[4])
print(string[5:13])
print(string[:5])
print(string[5:])
print(string1[1])

#String Indexing
#We can access individual elements from strings using indexing, which starts at zero and goes up to n-1
#where n is the total number of characters in the string minus one. Here's how it works for

str1 = 'HELLO PYTHON'
print(str1)
print(str1[0])
#Output: H

Str1 = 'HELLO PYTHON'
print(Str1[-4:-2])  #Max negative value at first index position, Min negative value at the second index position
print(Str1[-2:-1])

#Different Operations on String

#1. Upper() method
#This method returns the UPPER CASE version of the string.
string = 'Personal Handbook!'
print(string.upper())  

#Result: 'PERSONAL HANDBOOK!'

#2. Lower() method
#This method returns the lower case version of the string.
string = 'EPAT Handbook!'
print(string.lower())
#Result: 'epat handbook!'

#3. strip() method
#This method returns a string with whitespace removed from the start and end.
string = ' A string with whitespace at both \
the ends. '

print(string.strip())

#4.isalpha() method
#This method returns the boolean value True if all characters in a string are letters, False otherwise.
string = 'Alphabets'.isalpha()
print (string) #True

string = 'Alphabets123'.isalpha()
print (string) #False

string = 'Thisstringcontainsonlyalphabets'
print(string.isalpha()) #Ture

string = 'This string contains only alphabets'
print(string.isalpha()) #False

#5. isdigit() method
#This method returns the boolean value True if all characters in a string are digits, False otherwise.
string = '12345'
print(string.isdigit())

string = 12345
print(string.isdigit())

#6. startswith(argument) method
#This method returns the boolean value True if the first character of a string starts with the character provided as an argument, False otherwise.
string = 'EPAT Handbook!'
print(string.startswith('E')) #True

string = 'EPAT Handbook!'
print(string.startswith('e')) #False

string = 'EPAT Handbook!'
print(string.startswith('')) #False

#7. endswith(argument) method
#This method returns the boolean value True if the last character of a string ends with the character provided as an argument, False otherwise.
string = 'EPAT Handbook!'
print(string.endswith('')) #False 

string = 'EPAT Handbook!'
print(string.endswith('!')) #True 

#8. find(substring, start, end) method
#This method returns the lowest index in a string where substring sub is found within the slice [start:end]. 
#Here, arguments start and end are optional. It returns -1 if sub is not found.
string='EPAT Handbook!'
print(string.find('EPAT',4,9)) # =1

string='EPAT Handbook!'
print(string.find('A')) # 2

string='EPAAT Handbook!'
print(string.find('A')) #2

string= 'EPAT Handbook!'
print(string.find('Z')) #-1
'''
#9. replace(old, new) method
#This method returns a copy of the string with all occurrences of old replace by new.
string = '00 01 10 11'
print(string.replace('0', '1')) # 11 11 11 11

#10. split(delimeter) method
#This method is used to split a string into multiple strings based on the delimeter argument.

string = 'Bike Car Bus'
print(string.split(' ')) #['Bike', 'Car', 'Bus']

string = '100.00.00.001.000'
print(string.split(' '))  #['100.00.00.001.000']

#11. index(character) method
#This method returns the index of the first occurrence of the character.
string = 'EPAT HandPPook!'
print(string.index('P')) #1

string = 'EPAT Handbook!'
print(string.index('Z')) #ValueError: substring not found

###### Write and practice till this ##########

'''
#12. capitalize() method
This method returns a capitalized version of the string.
string = 'python is amazing!'
print(string.capitalize())

#13. count(character) method
This method returns a count of an argument provided by character
string = 'EPAT Handbook'
print(string.count('o'))

#14. len() method
Returns length or number of characters in given sequence (String).
string = "Hello World"
length_of_str=len(string) # Output:  11
print(length_of_str)

String Operators:
- + : Concatenation Operator, used to join two strings together into one single entity
- * : Repetition operator which repeats each element n times where n can be any integer value
- In : In operator which helps us to find whether the string value is present or not.
- Not In: NotIn operator which helps us to find the string value is present or not.

+ Operator:
Msg1 = "Today is 1st day of class"
#"We are learning Python"
print (Msg1 + "We are learning Python")

* Operator:
Sample_string = 'Python! '
print(Sample_string)
print(Sample_string * 3)

In Operator:
name="John Doe"
print(name in 'My name is John Doe')

Not In Operator:
age =45
print(age not in 'my name is john Deo and my age is {age}')

s = 'Food'
print(s Not in 'Hello world')

#Float

str1 = 10.02
print(str1)

str1 = 20.00
print(str1*2)

str1 = 23.26
print(str1 - 10)


#Type() function
The inbuilt type(argument) function is used to evaluate the data type and returns the class type of the argument passed as a parameter

string = 'EPAT Handbook'
print(type(string))

a = 10023
print(type(a))

b = 100.02
print(type(b))

string = True
print(type(string))

string = False
print(type(string))

string = 'False'
print(type(string))

#List
string = [1,2,3]
print(type(string))

#Dictionary
string = {'name':'TechieSmiles'}
print(type(string))

#Tuple
string = (456,'Hello',True)
print(type(string))

#Set
string = {789,"Python",None} #Note: Sets cannot have duplicate values and they are unordered collection of elements
string = {789,"Python", "Programming"}
print(type(string))

#A list, dict, tuple, set are native data structures within Python.

#Data type Conversion
Converting data type from one to another type is called Data Type conversion. When we change the type of a
variable from one to another, this is called typecasting.

There can be two types of conversion possible: implicit termed as coercion, and explicit often referred to as casting.

#Implicit Conversion:
In Implicit Conversions, there's no need for explicit casting as it happens automatically during assignment.

print(8 / 2)
print(type(8 / 2)

#Explicit Conversion:
To perform an Explicit Conversion in python you can use various built-in functions like int(), float(), str(). Here's how they work

string = 'This is the year ' + 2023
print(string)

string = 'This is the year ' + str(2023)
print(type(string))

#String to Int Conversion
string = '400'
print(type(string))
print(type(int(string)))

#Int to String Conversion
a = 10
print(type(a))
print(type(str(a)))

#Int to Float conversion
a =10
print(type(a))
print(type(float(a)))

#String to Float conversion
string = '400'
print(type(string))
print(type(float(string)))

#Boolean to Int conversion
boolean_value=True
print(type(int(boolean_value))

boolean_value=False
print(type(int(boolean_value))

boolean_value=0
print(type(bool(boolean_value))

boolean_value=1
print(type(bool(boolean_value))

'''










