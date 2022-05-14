#################################
# if ... elif ... else Statements
# Execute a specific block of code if a condition is evaluated to True
#################################

a, b = 3, 5
if a < b:  # if a is less that b execute the indented block of code under the if clause, otherwise go and test the elif condition
    print('a is less than b')
elif a == b:  # if a is equal to b execute the indented block of code that fallows, otherwise execute the block of code under the else clause
    print('a is equal to b')
else:
    print('a is greater than b')


# or / and operators
your_age = 14
if your_age < 0 or your_age > 99:  # if ANY of the expression is True execute the indented block of code under the if clause
    print('Invalid age!')
elif your_age <= 2:
    print('You are an Infant')
elif your_age < 18:
    print('You are a child')
else:
    print('You are an adult')


a = 3
if 1 < a <= 9:
    print('a is greater than 1 and less than of equal to 9')

# equivalent to
if a > 1 and a <= 9:
    print('a is greater than 1 and less than of equal to 9')


a = 12
# The fallowing 3 exemples test if a number a is divisible by 6
# 1st Example - nested if
if a % 2 == 0:
    if a % 3 == 0:
        print('Example 1: a is divisible by 2 and 3 (or by 6)')


# 2nd Example: and operator -> it returns True if both expressions are True, False otherwise
if a % 2 == 0 and a % 3 == 0:
    print('Example 2: a is divisible by 2 and 3 (or by 6)')

# 3rd Example
if not (a % 2 and a % 3):  # the truthniness of an expression: a % 2 is equal to bool(a %2)
    print('Example 2: a is divisible by 2 and 3 (or by 6)')


# The truthiness of a variable
b = 0
if b:  # it test the truthiness of b or bool(b)
    print('The truthiness of b: True')
else:
    print('The truthiness of b: False')

my_str = 'some string'
if my_str:  # it test the truthiness of my_str or bool(my_str)
    print('The truthiness of my_str: True')
else:
    print('The truthiness of my_str: False')


name = 'Andrei'
# Pythonic version
print('Hello Andrei') if name == 'Andrei' else print('You are not Andrei!')

# equivalent to:
if name == 'Andrei':
    print('Hello Andrei')
else:
    print('You are not Andrei')
