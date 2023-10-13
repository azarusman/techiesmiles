# List Comprehensions
# 1. List comprehension is an elegant way to define and create a list in Python. 
# 2. It is used to create a new list from another sequence, just like a mathematical set notation in a single line.
# 3. List comprehension starts and ends with square brackets to help us remember that the output will be a list.

# Syntax: [output expression for item in sequence if condition]
'''
# Example 1: Cubic validation
cube_list = []

for i in range(0,10):
    cube_list.append(i**3)
print(cube_list)

# Same program in List comprehension method
x = [i**3 for i in range(0,10)]
print(x)


# Example 2: Number which is divisible by 2 and 3
cube = []
for i in range(0,20):
    if i%2==0 and i%3==0:
        cube.append(i)
print(cube)

# Same program in List Comprehension method
x = [i for i in range(0,20) if i%2==0 if i%3==0]
print(x)

# Example 3: Odd or Even numbers
a = []
for i in range(1,11):
    if i%2==0:
        print(str(i) + ' Even')
    else:
        print(str(i) + ' Odd')

# Same program in List Comprehension method
x= [str(i) + ' Even' if i%2==0  else str(i) + ' Odd'   for i in range(1,11)]
print(x)

'''
# Example 4: Multiplication
for i in range(1,11):
    for j in range(7,8):
        print(f'7*{i}= {i*j}')

# Same program in Comprehension method
x = [ f'7*{i}= {i*j}' for i in range(1,11) for j in range(7,8)]
print(x)

# A list comprehension returns list. 
# It consists of square brackets containing an expression that gets executed for each element in the iteration over a loop.

'''
# can we use while loop in list comprehesion?
No, you cannot use a while loop directly within a list comprehension. 
List comprehensions in Python are designed to create new lists by iterating over an existing iterable (e.g., a list or range) and applying an expression to each item. 
The iteration is done using for loops, not while loops.


# While loop

end = 10
count = 1

while count<=end:
    print(count)
    count+=1
    if count==6:
        break

# Using List comprehension
end = 10
result = [count for count in range(1, end + 1) if count <= 5]
print(result)

'''





    