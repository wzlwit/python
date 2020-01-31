""" 
Exception Type Description
IOError             Raised when an I/O operation fails, such as when an attempt is made to open a nonexistent file in read mode.
IndexError          Raised when a sequence is indexed with a number of a nonexistent element.
KeyError            Raised when a dictionary key is not found.
NameError           Raised when a name (of a variable or function, for example) is not found.
SyntaxError         Raised when a syntax error is encountered.
TypeError           Raised when a built-in operation or function is applied to an object of inappropriate type.
ValueError          Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
ZeroDivisionError   Raised when the second argument of a division or modulo operation is zero.
"""

# Handle It
# Demonstrates handling exceptions
# try/except
try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")


# specifying exception type
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")


# handle multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")


print()
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")


# get an exception's argument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say...")
    print(e)


# try/except/else
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:                   # The else block executes only if no exception is raised in the try block.
    print("You entered the number", num)

# input("\n\nPress the enter key to exit.")