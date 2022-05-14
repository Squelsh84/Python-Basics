########################
# String Methods
########################

dir(str)        # => lists all string methods
help(str.find)  # => displays the help of a method

# All string methods return a new string but don't modify the original string
my_str = 'I learn Python Programming'
my_str.upper()        # => 'I LEARN PYTHON PROGRAMMING'
my_str.lower()        # => 'i learn python programming'

my_ip = '  10.0.0.1 '
my_ip.strip()       # => '10.0.0.1'

my_ip = '$$$10.0.0.1$$'
my_ip.strip('$')        # => '10.0.0.1'

# Removes all leading whitespace in string
my_ip.lstrip()      # => '10.0.0.1 '

# Removes all trailing whitespace of string
my_ip.rstrip()      # => '  10.0.0.1'

my_str = 'I learn Python'
my_str.replace('Python', 'Go')     # => 'I learn Go'

# split() returns a list from a string having a delimiter
my_ip.split('.')            # => ['10', '0', '0', '1']

# Be default the delimiter is a whitespace
# => my_list = ['I', 'learn', 'Python', 'Programming']
my_list = my_str.split()

# join() returns a string from a list
':'.join(my_list)       # => '10:0:0:1'

# in and not in operators test membership
'10' in my_ip           # => returns True
'10' not in my_ip       # => returns False
'20' in my_ip           # => returns False


# Other string methods
my_str = 'this is a string. this is a string'

# Returns the first index in my_str where substring 'is' is found or -1 if it didn't find the substring
my_str.find('is')       # => 2
my_str.find('si')       # => -1

# Returns a capitalized version of the string.
my_str.capitalize()     # => 'This is a string. this is a string'

# Returns True if my_str is an uppercase string, False otherwise
my_str.isupper()        # => False

# Returns True if my_str is a lowercase string, False otherwise
my_str.lower().islower()    # => True

# Returns the number of occurrences of substring 's' in my_str
my_str.count('s')       # => 6

'0123123'.isdigit()     # => True
'0123123x'.isdigit()    # => False
'abc'.isalpha()         # => True
'0123123x'.isalnum()    # => True

my_str1 = 'Hi everyone!'
# Inverts case for all letters in string
my_str1.swapcase()      # => 'hI EVERYONE!'
