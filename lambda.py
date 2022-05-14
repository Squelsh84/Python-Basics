#########################
# Lambda Expressions
#########################

# "x" and "y" are lambdas arguments.
def add(x, y): return x + y    # this creates a function


type(add)                   # => function


# Assigning lambda expression to a variable
result = add(2, 3)      # => 5


# We can use default arguments
def add(x=1, y=0): return x + y


result = add()      # => 1


# We can even use *args and **kwargs
my_function = lambda x, *args, **kwargs: (x, *args, {**kwargs})
# x is 2.3, args is (a, b, c) and kwargs is {arg1='abc', arg2='def', arg3='geh'}
my_function(2.3, 'a', 'b', 'c', arg1='abc', arg2='def', arg3='geh')


# Passing as an argument to a function
# Lambdas are functions and can therefore be passed to any other function as an argument (or returned from another function)
def my_func(x, fn):
    return fn(x)


result = my_func(2, lambda x: x**2)
print(result)       # => 4

result = my_func(2, lambda x: x**3)
print(result)       # => 8

result = my_func('a', lambda x: x * 3)
print(result)       # => 'aaa'

result = my_func('a:b:c', lambda x: x.split(':'))
print(result)       # => ['a', 'b', 'c'] -> this is a list

result = my_func(('p', 'y', 't', 'h', 'o', 'n'), lambda x: '-'.join(x))
print(result)       # => p-y-t-h-o-n > this is a string
