#################################
# While Loops
#################################

a = 10
# Infinite Loop, it prints out 10 indefinitely

# while a:  #it tests the truthiness of a or bool(a) which is always True
#    print(a)

# Prints out numbers from 10 to 1
while a:    # => "while a:" is equivalent to "while a > 0:"
    print(a)
    a -= 1
# => executes the below block of code after finishing the while looop (and if no "break" statement has been executed)
else:
    print('Finishing printing numbers. a is now 0')


# it prints out only odd numbers between 1 and 20
a = 0
while a < 20:
    a += 1
    if a % 2 == 0:
        continue    # go the the beginning of the while loop
    # it reaches this line only if the continue statement hasn't been executed
    print(f'Odd number {a}')


# it prints out numbers greater than 2
a = 7
# While Loops
#################################

a = 10
# Infinite Loop, it prints out 10 indefinitely

# while a:  #it tests the truthiness of a or bool(a) which is always True
#    print(a)

# Prints out numbers from 10 to 1
while a:    # => "while a:" is equivalent to "while a > 0:"
    print(a)
    a -= 1
# => executes the below block of code after finishing the while looop (and if no "break" statement has been executed)
else:
    print('Finishing printing numbers. a is now 0')


# it prints out only odd numbers between 1 and 20
a = 0
while a < 20:
    a += 1
    if a % 2 == 0:
        continue    # go the the beginning of the while loop
    # it reaches this line only if the continue statement hasn't been executed
    print(f'Odd number {a}')


# it prints out numbers greater than 2
a = 7
while a > 0:
    a -= 1
    if a == 2:
        break   # => it breaks out of the while loop and executes the next instruction after the while block of code
    print(a)

print('Loop ended.')
while a > 0:
    a -= 1
    if a == 2:
        break   # => it breaks out of the while loop and executes the next instruction after the while block of code
    print(a)

print('Loop ended.')
