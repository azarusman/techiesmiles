#Python Loops
'''
A loop is a fundamental programming construct that allows you to execute a certain block of code repeatedly, 
either for a specified number of times or until a certain condition is met. 
Loops are used to automate repetitive tasks and make the code more efficient and concise.

There are two main types of loops in programming: For loops and While loops.

For Loop:
A for loop is used to iterate over a sequence (such as a list, tuple, or range) a specific number of times. 
It consists of an initialization, a condition, and an increment (or decrement) statement. 
The loop runs as long as the condition is satisfied.

for element in sequence:
    # Code to be executed for each element

While Loop:
A while loop is used to repeatedly execute a block of code as long as a specified condition remains true. 
It doesn't require a predetermined number of iterations; it keeps running as long as the condition is met.

while condition:
    # Code to be executed as long as the condition is true

#For Loop

i = [1,2,3,4,5]
for a in i:
    print(a)

for i in range(1,10+1):
    print(i)

for i in range(5,50,5):
    print(i)

for i in range(100,5-5,-5):
    print(i)
else:
    print('over')

#List in For loop
a = [2,4,6,8,10]
for i in a:
    print(i*i)

#List using String in For loop

a = ['volvo',12,4,5.5,'BMW']
for i in a:
    print(i*3,' ')

#Reading a file
filepath='C:/Users/Elait141/Desktop/Techie Smiles/Python/Files/Python_File.txt'

try:
    with open(filepath,'r') as f:
        
        for i in f:
            if i>3:
                break

except FileNotFoundError:
    print("File not found")

#Tuple using For loop
a = ('volvo', 12,1,1.5,True,'BMW')

for i in a:
    if type(i)==int or type(i)==float:
        print(f'(This is integer and float {type(i)}')
    else:
        print (type(i))

filepath='C:/Users/Elait141/Desktop/Techie Smiles/Python/Files/Python_File.txt'

try:
    with open(filepath,'r') as f:
        for line_num, line in enumerate(f):
            if line_num<3:
                print(line)
            else:
                break
except FileNotFoundError:
    print('File not found')

#The enumerate() function is used to iterate over both the line number and the line content from the file.
#The line_num variable keeps track of the line number, starting from 0.
#The loop reads each line and prints it using print(line.strip()), where strip() is used to remove the newline character from the end of each line.
'''
#While Loop
'''
The while statement in Python is used to repeat execution of code or block
of code that is controlled by a conditional expression. The syntax for a whileloop is given below:

A while statement allows us to repeat code execution until a conditional
expression becomes true.

data_points = 6
count = 0
while count != data_points:
print(count)
count += 1

The while statement is an example of what is called a looping statement.

#Printing the values till 6
data_points = 6
count = 0

while count <= data_points:
    print(count)
    count+=1
else:
    print("While loop is over")

#Reading a file using While loop
file_path = 'C:/Users/Elait141/Desktop/Techie Smiles/Python/Files/Python_File.txt'
try:
     
    with open(file_path,'r') as f:
        line = f.readline()
        while line:
            print(line.strip())
            line = f.readline()
except FileNotFoundError:
    print("File not found")

#Driving a car
speed = 0
max_speed_limit = 60

while speed <= max_speed_limit:
    print(f'Cureent speed limit is {speed}')
    speed+=20

#ATM Pin
pin_code = "1234"

while True:
    user_input = input("Enter your PIN code: ")
    if user_input == pin_code:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN. Try again.")
'''
correct_pin = '1234'
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter your ATM PIN: ")
    
    if user_input == correct_pin:
        print("Access granted!")
        break  # Exit the loop if the correct PIN is entered
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect PIN. You have {remaining_attempts} attempts left.")
        
if attempts == max_attempts:
    print("Maximum attempts reached. Your card is blocked.")
