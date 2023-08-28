

#Type Error
def myfunc(x):
    try:
        #TypeError
        y = 6
        z = x + y # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'
        print(z)

        #IndexError
        try:
            a=[1,2,3,4,5]
            print(a[1])

        except IndexError:
            print('Mentioned value is out of range')
        

        #KeyError
        a = {'Location':'America','Salary':123, 'Dept':'IT'}
        print(a['Location']) #KeyError: 'JoiningDate'

        #ZeroDivisionError
        # initialize the amount variable
        marks = 10000

        # perform division with 0
        a = marks // 0
        print(a) #ZeroDivisionError: division by zero

    except TypeError:
        print('Please enter integers')
    except KeyError:
        print('Entered Key value is not present')
    except FileNotFoundError:
        print('File is not available')
    except ImportError:
        print('Import the corrrect libraries')
    except ZeroDivisionError:
        print('Please enter other than 0 and alphabets')
    

myfunc(x=6)


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
	
