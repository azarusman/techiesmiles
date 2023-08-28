#File Handling
'''
Python too supports file handling and allows users to handle files 
i.e., to read and write files, along with many other file handling options, to operate on files.

Syntax
f = open(filename, mode) 

Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. 
    If the file already contains some data then it will be overridden but if the file is not present 
	then it creates the file as well.
a:  open an existing file for append operation. It won't override existing data.
r+:  To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won't override existing data.

# A file named "python File", will be opened with the reading mode.
filepath = "C:\\Users\\Elait141\\Desktop\\Techie Smiles\\Python\\Files\\Python file.txt"
file = open(filepath, 'r')

# This will print every line one by one in the file
for each in file:
	print (each)
	
# Python code to illustrate with()
with open(filepath) as file:
	data = file.read()

print(data)

#File reading functions
#read(): Reads the entire content of the file as a single string.
#readline(): Reads a single line from the file and advances the file pointer.
#readlines(): Reads all lines from the file and returns them as a list of strings.

#File writing functions
#write(): That enable you to write data to a file.

#File close
#close(): The close() function is used to close an open file in Python. 
#It's important to close files after you're done using them to free up system resources and ensure that changes you've made to the file are saved.
	
#Writing a data into the existing file 

# Python code to create a file
file = open(filepath,'w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#Import os 
#what is import os?
. os is a built-in module in Python that provides a way to interact with the operating system's functionalities. 
. It allows you to perform various tasks related to file and directory manipulation, environment variables, process management, and more. 
. With the os module, you can create, delete, rename, and manipulate files and directories, get information about the system, and execute system commands.

Some basic operation performed using os are:

1. File and directory operations: Creating, deleting, renaming, and checking file/directory existence.
2. Environment variables: Accessing and modifying environment variables.
3. Path handling: Joining, splitting, and normalizing paths.
4. Process management: Spawning new processes, getting process information, and more.

import os

directory = "C:\\Users\\Elait141\\Desktop\\Techie Smiles"
files = os.listdir()

print("Files in the directory:")
for file in files:
    print(file)
'''

import os

filename = "C:\\Users\\Elait141\\Desktop\\Techie Smiles\\Python\\Files\\PythonFile1.txt"
new_filename = "C:\\Users\\Elait141\\Desktop\\Techie Smiles\\Python\\Files\\PythonFile.txt"

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + "successfully.")
	except IOError:
		print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)

create_file(filename)
read_file(filename)
append_file(filename, "This is some additional text.\n")
read_file(filename)
rename_file(filename, new_filename)
read_file(new_filename)
#delete_file(new_filename)