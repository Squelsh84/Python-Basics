#############################
## Comparison and Identity Operators
#############################
 
# Assignment is =
a = 2
b = 3
 
# Equality is == and compares the values stored by the variables
a == b  # => False
b == b  # => True
 
# Inequality is !=
a != b  # => True
 
# More comparisons
a > b   # => False
5 >= 5  # => True
b <= a  # => False
 
'Python' == 'python'    # => False - case matters
 
id(a)   # => returns the address where the value referenced by a is stored 140464475242000
 
#is checks if two variables refer to the same object (saved at the same memory address)
a is b  # => False = compares the address of a to the address of b