#################################
## Boolean Variables
#################################
 
## True equals 1 and False equals 0
True == 1   # => True
bool(True)  # => 1
 
False == 0  # => True
bool(False) # => 0
 
 
1 is True   # => False
0 is False  # => False
 
 
True > False    # => True
a = (True + True ) * 10     # => 20
 
id(True)    # => 10714848 (you'll obtain another value)
id(4 > 2)   # => 10714848  - the address of True and False is constant during program execution
 
#The next 2 expressions are equivalent
(4 > 2) == True     # => True
(4 > 2) is True     # => True
 
 
## Truthiness of objects
bool(0)     # => False
bool(0.0)   # => False
bool(10)    # => True
bool(-1.5)  # => True
 
bool('')    # => False (empty string)
bool('py')  # => True
 
bool([])    # => False (empty list)
bool([1,2]) # => True
 
bool(())    # => False (empty tuple)
bool((3,4)) # => True
 
bool({})        # => False (empty dictionary)
bool({1:'abc',2:55,'a':5})   # => True