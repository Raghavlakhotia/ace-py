# Exception handling.
# --------------------------------------------------------

try:
    print("Yeah ! Your answer is :", result)
except Exception as e:
        print("The error is: ",e)

# Raise an exception.
# --------------------------------------------------------

if x < 0:
  raise Exception("Sorry, no numbers below zero")


# User defined exception.
# --------------------------------------------------------

class MyZeroDivisionError(Exception):
    def __init__(self, message="Division by zero is not allowed."):
        self.message = message
        super().__init__(self.message)

# Rasie exception
def divide(x, y):
    if y == 0:
        raise MyZeroDivisionError("Cannot divide by zero.")
    return x / y

# Handle exception.
try:
    result = divide(10, 0)
except MyZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")


'''
Some of the common Exception Errors are : 
 

IOError:            if the file can’t be opened
KeyboardInterrupt:  when an unrequired key is pressed by the user
ValueError:         when the built-in function receives a wrong argument
EOFError:           if End-Of-File is hit without reading any data
ImportError:        if it is unable to find the module
'''






