#################################
# Intro to Functions
#################################

# Use "def" to create new functions
def my_function1():
    """
    This is function's docstring.
    """
    print('This is a function!')
    # this function returns implicitly None


# Calling the function
my_function1()           # => This is a function!
my_function1.__doc__     # => This is function's docstring.


# return exits the function
def my_function2():
    x = 1
    return x                             # the function ends here
    print('Never reaches this line!')   # it will never execute this line


# Calling the function
my_function2()      # returns 1


# A function can return more values as a tuple
def add_multiply_power(x, y):
    return x + y, x * y, x ** y


# Calling the function
a, b, c = add_multiply_power(2, 3)  # returns (2 + 3, 2 * 3, 2 ** 3)
print(a, b, c)                      # => 5 6 8

########################
# Function's Arguments
########################

# Function with positional arguments


def add(x, y):
    print(f"x is {x} and y is {y}")
    return x + y  # Returns the result of x + y with a return statement


# Calling function with positional arguments
s = add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11, s is 11

# Calling function with keyword arguments
s = add(y=1, x=8)  # => prints out "x is 8 and y is 1" and returns 9, s is 9


# Function with default arguments
def add(x=1, y=0):
    print(f"x is {x} and y is {y}")
    return x + y  # Returns the result of x + y with a return statement


# Calling function with default arguments
s = add()     # => prints out "x is 1 and y is 0" and returns 1, s is 1
s = add(5)    # => prints out "x is 5 and y is 0" and returns 5, s is 5
s = add(5, 3)  # => prints out "x is 5 and y is 3" and returns 8, s is 8

# Wrong way to define a function => SyntaxError: non-default argument follows default argument
# def my_function(a, b=5, c):
#     print(a, b, c)


# Function that takes a variable number of positional arguments
def concatenate(*args):
    result = ''
    for tmp in args:
        result = result + tmp
    return result


# Calling the function
result = concatenate()
print(result)           # => '' -> empty string

result = concatenate('Python', '!')
print(result)           # => Python!

result = concatenate('I', 'love ', 'programming')
print(result)          # => Ilove programming


# Function that takes a variable number of keyword arguments
def device_info(**kwargs):  # kwargs is a dictionary
    for k, v in kwargs.items():
        print(f'{k}: {v}')


# Calling the function
# It prints out:
# ip: 10.0.0.1
# username: u1
# password: secretpass
device_info(name='Cisco Router', ip='10.0.0.1',
            username='u1', password='secretpass')
