#################################
# User Input and Type Casting
#################################

# Simple way to get user input from console
input_string_var = input("Enter some data: ")  # Returns the data as a string

# To perform arithmetic operations we must cast to int or float
a = input('Enter a:')       # => a stores string
b = int(input('Enter b:'))  # => b stores an int
c = float(a) * b            # => here I multiply a float by an int


# Type casting
a = 3       # => type int
b = 4.5     # => type float
c = '1.2'   # => type str

print('a is ' + str(a))     # => str(a) returns a string from an int
print('b is ' + str(b))     # => str(b) returns a string from a float
d = b * float(c)            # => here I multipy 2 floats. d is a float.

str1 = '12 a'
# float(str1)    # => error
