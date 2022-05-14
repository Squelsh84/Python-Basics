#################################
# For Loops
#################################

movies = ['Star Wars', 'The Godfather', 'Harry Potter ', 'Lord of the Rings']

for m in movies:  # it iterates over a sequence and executes the code indented under the "for" clause for each element in the sequence
    print(f'One of my favorites movie is {m}')
# the indented code below "else" will be executed when "for" has finished looping over the entire list (no "break" statement executed)
else:
    print('This is the end of the list')


for i in range(100):
    pass    # => empty instruction or "no nothing"

for i in range(10):  # => from 0 (default, included) to 10 excluded
    print(i, end=' ')
# it prints out:  0 1 2 3 4 5 6 7 8 9

for i in range(3, 9):  # => from 3 included to 9 excluded
    print(i, end=' ')
# it prints out: 3 4 5 6 7 8


for i in range(3, 20, 3):  # => from 3 included to 20 excluded in steps of 3
    print(i, end=' ')
# it prints out: 3 6 9 12 15 18


# for ... continue -> it prints out all letters of the string without 'o'
for letter in 'Python Go and Java Cobol':
    if letter == 'o':
        continue  # go to the beginning of the for loop and do the next iteration
    print(letter, end='')


# for ... break
sequence = [1, 5, 19, 3, 31, 100, 55, 34]
for item in sequence:
    if item % 17 == 0:
        print('A number divisible by 17 has been found! Breaking the loop...')
        # breaks out of the loop (executes the first instruction (if any) after the else block of code)
        break
else:
    print('There is no number divisible by 17 in the sequence')
