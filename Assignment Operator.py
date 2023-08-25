#Python Assignment Operator
'''
# += Operator
a, b = 5, 7

#a = a + 2
#b = b - 2
a+=2
b-=2

print(a) #7
print(b) #5
print(a,b) #7,5
print(a+b) #12
print(a*b) #35
print(a-b) #2
print(a/b) #1.4

# How the above process works
a = a+2

# -= Operator
a-=2

# How the above process works
a = a-2
print(a)

# *= Operator
a*=2
print(a)

# %= Operator
a%=2
print(a)

#/= Operator
a/=2
print(a)

a = 5
print(a)

a**=3 
print(a) 
print(a*a*a)

a = 2 + 5 - 3 + 1
print(a) #5

a = 2 + 5 * 3
print(a) #17

a = (2 * 3) + (3 - 5)
print(a) #8 #4

#Control Flow Statments

Control flow statements in Python are used to change the order of execution of a program. 
They are used to make decisions, repeat code, and jump to different parts of a program.

There are three main types of control flow statements in Python:

Conditional statements** are used to make decisions based on the value of a condition. 
The most common conditional statement is the `if` statement.

Loop statements** are used to repeat a block of code a certain number of times or until a condition is met. 
The most common loop statements are the `for` loop and the `while` loop.

Jump statements** are used to jump to a different part of a program. 
The most common jump statements are the `break` statement and the `continue` statement.


#IF Conditional Statement

#The if statement is used when we want a code to be executed under certain conditions only.
#It can be either a single condition or multiple conditions. 
#The code within the if block will be executed if and only if the logical conditions are held true. 

#Program 1

a = 15; b = 10

#Example 1
if (a>=b):
    print("a is greater than or equal to b")
else:
    print('b is greater')


#Example 2
if (a>b):
    print("a is greater than b")
elif(a==b):
    print ("a equals to b ")
else:
    print('b is greater')


#In Python, we use the colon : to mark the end of the statement and start of the block. 
#This is true for any statement such as a class or function definition, conditional statements, loops, etc.

#Program 2 
#Runtime input from user

num = int(input('Hello! Please enter your input: '))

if (num>0):
    print('Positive Number')
elif (num<0):
    print("Negative Number")
elif (num==0):
    print ('Number Zero!')
else:
    print('Invalid input')

#Program 3
#Runtime Input from User

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#Program 4
#Runtime Input from User
#Determine Larget numbers?

num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
num3 = int(input('Enter the 3rd number: '))

if ( num1 >= num2) and (num1 >= num3):
    print(f'{num1} is greater than {num2} & {num3}')
elif( num2 >= num1) and (num2 >= num3):
    print(f'{num2} is greater than {num1} & {num3}')
else:
    print(f'{num3} is greater number')


#Program 5
#Runtime Input from User
#Find out if it's an even/odd number
number=int(input('Enter input: ')) #Inputting the value in variable 'number'
if ((number%2)==0 ):
    print ("It is Even")
else :
    print ("It is Odd")

#Program 6
#Calculating student marks
#Verifying the student marks based on Average

Tam = int(input('Enter the Tamil marks '))
Eng = int(input('Enter the Eng marks '))
Mat = int(input('Enter the Mat marks '))
Sci = int(input('Enter the Sci marks '))
Soc = int(input('Enter the Soc marks '))

Average = 35

Total_marks = Tam+Eng+Mat+Sci+Soc
print(Total_marks)

Ave_mark = Total_marks/5
print(Ave_mark)

if (Ave_mark>=Average):
    print('Pass')
else:
    print("Fail")

#Verifying the student status based on Subject and total average

Tam = int(input('Enter the Tamil marks '))
Eng = int(input('Enter the Eng marks '))
Mat = int(input('Enter the Mat marks '))
Sci = int(input('Enter the Sci marks '))
Soc = int(input('Enter the Soc marks '))

Average = 35

Total_marks = Tam+Eng+Mat+Sci+Soc
print(Total_marks)

Ave_mark = Total_marks/5
print(Ave_mark)

if (Tam & Eng & Mat & Sci & Soc >=35) and (Ave_mark>=Average):
    print('Pass')
else:
    print("Fail")
'''
#Program 7
#Reading the content from a file 

filepath='C:\\Users\\Elait141\\Desktop\\Techie Smiles\\Python\\Files\\Python File.txt'

# / = Forward slash -- In all programming language, it is suggested to give forward slash to avoid confusion. 
#how to read specific line from a file?

try:
    with open(filepath,'r') as f:
        line = f.readlines()

        if line:
            print("Below are the contents:")
            for i in range(1):
                print(f"{i} : {line[i]} ")
            #print(f'Number of lines present {len(line)}')
        else:
            print("File is empty!")

except FileNotFoundError:
    print("File is not present")
'''
#Program 8
#Writing the content to a new file 

filepath= 'C:/Users/Elait141/Desktop/Techie Smiles/Python/Files/Python File.txt'

try:
    with open(filepath,'r') as f:
        line = f.read()
        print(line)

except ConnectionError: 
    print("Connectivity Error")


#Program 9
#Appending new data into the existing file 

filepath='C:/Users/Elait141/Desktop/Techie Smiles/Python/Files/Python File.txt'

try:
    with open(filepath,'a') as f:
        f.write("\n Hi, This is my 3rd line")
        f.write("\n This is my 4th line")

except FileNotFoundError:
    print('File not found')


filepath='C:/Users/Elait141/Desktop/Techie Smiles/Python/Files/Python File.txt'
value = '3rd'
try:
    with open(filepath,'r') as f:
        found = False

        for line in f:
            if value in line:
                found = True
                break

        if found:
            print(f'{value} is present in the file')
        else:
            print(f'{value} is not present in the file')

except FileNotFoundError:
    print("File is not available")

    '''