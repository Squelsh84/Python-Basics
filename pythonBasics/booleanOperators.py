#################################
## Boolean Operators
#################################
# exp1 and exp2 -> True when both expressions are True and False otherwise
# exp1 or exp2  -> True when any expression is True
 
 
a, b = 3, 5
 
a < 10 and b < 10       # => True
a < 10 and b > 10       # => False
 
a < 10 or b < 10        # => True
a < 10 or b > 10        # => True
 
 
# The next 2 expressions are equivalent
2 < a < 6
2 < a and a < 6         # more readable
 
a != 7 or b > 100       # => True
 
not a == a              # => False
a == 3 and not b == 7   # => True
 
not a > 10 and b < 10       # => True
 
 
a < 10 or b > 10            # => True
not a < 10 or b > 10        # => False
not (a < 10 or b > 10)      # => False
 
 
# !!!!!!!!!!!
# Python considers in fact 4 > 2 and 2 == True.
4 > 2 == True         # => False
(4 > 2) == True       # => True