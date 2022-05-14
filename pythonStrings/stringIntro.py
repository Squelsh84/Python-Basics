#################################
# Intro to Strings
#################################

# strings (str objects) are enclosed by single or double quotes (' or "). Just be consistent within your code!
message1 = 'I love Python Programming!'
message2 = "I love Python Programming!"

# print() function displays the content of the string variable at console
print(message1)

# hello1 = 'Hi there! I'm Andrei'   # => error, cannot use ' inside ' ' or " inside " "
hello1 = 'Hi there! I\'m Andrei'    # => correct. ' inside ' ' must be escaped  using \
hello2 = "Hi there! I'm Andrei"     # you can use ' inside " " or " inside ' '


# Instructions between """ or ''' are treated as comments. It's recommended to use # to comment individual lines
"""
This is a multiline comment
a = 5
print(a)
Comment ends here.
"""

# This is a multiline string
languages = """ I learn Python,
Java, 
Go, 
PHP.
"""
print(languages)

# \n is a new line
print('Hello \nWorld!')     # => it displays Hello World! on 2 lines

# \ is used to escape characters that have a special meaning
info = '\\ character is used to escape characters that have a special meaning'
# => \ character is used to escape characters that have a special meaning
print(info)
