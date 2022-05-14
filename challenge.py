# Challenge #1

# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.

x = int(input("Enter a number: "))
all_divisors = list()
for i in range(2, x//2+1):
    if x % i == 0:
        all_divisors.append(i)

print(all_divisors)

# Challenge #2

# Consider the following string: nums = '10,20,30,40,50'

# Create a Python script that creates a list of integers from the string.

# The resulting list will be: [10, 20, 30, 40, 50]

nums = '10,20,30,40,50'
nums_list = nums.split(',')
print(nums_list)  # => ['10', '20', '30', '40', '50']

nums1 = [int(n) for n in nums_list]
print(nums1)    # => [10, 20, 30, 40, 50]

# Challenge #3

# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.

nums = list()

for i in range(1500, 3201):
    if i % 7 == 0 and i % 5 != 0:
        nums.append(str(i))

print(','.join(nums))

# Challenge #4

# Write a program that asks the user for a long string containing multiple words separated by whitespaces.

# Make it to print back the same string with the words in backward order.

# For example, say I type the string: My name is Andrei

# Then the script should print out: Andrei is name My
words = input('Enter some words:')
words_list = words.split(' ')
# print(words_list)
words_reversed = ' '.join(reversed(words_list))
print(words_reversed)


# Challenge #5

# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

# Sample input string : green-red-yellow-black-white

# Expected Result : black-green-red-white-yellow


string = input("Enter a hyphen-separated string: ")
words = string.split("-")
sorted_words = sorted(words)
sorted_str = "-".join(sorted_words)

print(sorted_str)


# Challenge #6

# Write a Python program that accepts as input a sequence of words separated by one or more whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.

# Sample input string: I love cat and dogs

# Expected Result : I evol tac dna sgod


string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
i = 0
for w in words:
    words[i] = w[::-1]
    i += 1

new_str = ' '.join(words)

print(new_str)

# Challenge #7

# Create an alternative solution for the previous challenge that uses list comprehension.

string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
words = [w[::-1] for w in words]

new_str = ' '.join(words)

print(new_str)


# Challenge #8

# Consider a list of words(strings). Write a Python script that generates a list of tuples where the first element of the tuple is the word in the list and the second element is its length.

# Use list comprehension if possible.

# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

# Expected Result: [('Python', 6), ('Java', 4), ('C++', 3), ('Golang', 6), ('Solidity', 8), ('Bash', 4)]

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

words_and_length = [(w, len(w)) for w in words]

print(words_and_length)


# Challenge #9

# Consider a list of words(strings). Write a Python script that generates a dictionary where the key is the word in the list and the value is its length.

# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']


words_and_length = dict()

for w in words:
    words_and_length[w] = len(w)

print(words_and_length)


# Challenge #10

# Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].

# Create a Set that contains the elements of the 2 lists in pairs.

# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}

names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]

names_and_phones = set(zip(names, phones))
print(names_and_phones)


# Challenge #11

# Consider the two Python lists. Write a Python Script to make a new list whose elements are the intersection of the two given lists. This means all elements of L1 that also belong to L2, but no other elements.

L1 = [1, 2, 5, 10, 11, -10, 9, 88]
L2 = [88, 5, 10, 6, 7]

L3 = list(set(L1).intersection(set(L2)))
print(L3)
