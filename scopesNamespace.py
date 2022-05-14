#################################
## Scopes and Namespaces
#################################
x = 3   # this is a global scoped variable


def my_func1():
    print(f'x is {x}')  # this is "x" variable from the global namespace


# Calling the function
my_func1()      # => x is 3


def my_func2():
    x = 6               # this is a local scoped variable
    print(f'x is {x}')  # this is NOT "x" variable from the global namespace


# Calling the function
my_func2()      # => x is 6
print(x)        # => 3 -> "x" variable was not modified inside the function


def my_func3():
    global x    # importing x variable from the global namespace
    x = x * 10  # this is "x" variable from the global namespace
    print(f'x is {x}')


# Calling the function
my_func3()      # => x is 30
print(x)        # => 30 -> global "x" variable was modified inside the function


def my_func4():
    print(f'x is {x}')
    x += 7      # this is an error, we used local x before assignment


# Calling the function
my_func4()      # => UnboundLocalError: local variable 'x' referenced before assignment
