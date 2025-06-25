# Beneath each comment write the code and print out the result to check it works

'''LISTS'''

# Create a list and assign it to a variable
lists = [6, 7, 0, 1, 2, 3, 4]

# Find the length of the list
length = len(lists)

# Append an item to the list
lists.append(5)

# Find the value of an item in the list a specific index
lists[2]

# Set the value of an item at a specific index
lists[2] = 123

# Check whether an item is in the list
if 123 in lists:
    print('123 is in lists')

# Sort the list

# Selection Sort:
lists = [2, 3, 4, 1, 2]
lists_sorted = []
# min_value= lists[0]
for i in range(len(lists)):
    min_value= float('inf')
    for j in range(i, len(lists)):
        if lists[j] < min_value:
            min_value = lists[j]
            min_index = j
    
    # Switch
    temp = lists[i]
    lists[i] = min_value
    lists[min_index] = temp

print(lists)

# Iterate over the list using range, printing out each element and the index

lists = [5, 4, 3, 2, 1]
for index in range(len(lists)):
    print(f'{index = }')
    print(f'{lists[index] = }')


# Iterate over the list without using range, printing out each element

for element in lists:
    print(f'{element = }')

'''TUPLES'''

# Create a tuple and assign it to a variable
tuples = (0, 9, 8, 7, 6)
print(f'{tuples = }')

# Find the length of the tuple
length_tuples = len(tuples)
print(f'{length_tuples = }')

# Find the value of an item in the tuple a specific index
print(tuples[1]) #9

# Check whether an item is in the tuple
if 0 in tuples:
    print('0 in tuples')

# Iterate over the tuple using range, printing out each element and the index
for i in range(len(tuples)):
    print('index is ', i)
    print(tuples[i])

# Iterate over the tuple without using range, printing out each element
for element in tuples:
    print('element is ', element)

'''STRINGS'''

# Create a string and assign it to a variable
strings = 'word'

# Find the length of the string
print(len(strings))

# Find the value of an character in the string a specific index
print(strings[0])

# Check whether an item is in the string
if 'w' in strings:
    print('w in strings')

# Concatenate (add) two strings together
new_strings = 'hello'
con_strings = new_strings + ' ' + strings
print(con_strings)

########## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
con_strings2 = ' '.join([strings, new_strings])
print(con_strings2)


# Create an f-string
con_strings3 = f'{strings} {new_strings}'
print(f'{con_strings3 = }')

# Split a string using .split
########## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
strings = 'I love food'
print(strings.split(' ')) # ['I', 'love', 'food']

# Join a list of strings using .join
lists_of_strings = ['I', 'like', 'swimming']
join_lists_of_strings = ' '.join(lists_of_strings)
print(f'{join_lists_of_strings = }')

# Iterate over the string using range, printing out each character and the index
strings = 'word'
for i in range(len(strings)):
    print('index is ', i)
    print(strings[i])

# Iterate over the string without using range, printing out each character
for letter in strings:
    print(letter)

'''DICTIONARIES'''

# Create a dictionary and assign it to a variable
dicts = {0:'A', 1: 'B', 2: 'C'}

# Find the length of the dictionary
print('length of dict is ', len(dicts))

# Add a new key/value pair
dicts[3] = 'D'

# Replace value for a given key
dicts[3] = 'F'

# Check whether a key is in the dictionary
if 0 in dicts:
    print('0 in dicts keys')

# Iterate over keys, printing each key
for key in dicts.keys():
    print('key is ', key)


# Iterate over over key/value pairs using .items(), printing each key and value
for key, value in dicts.items():
    print('key is', key)
    print('value is', value)


'''SETS'''

# Create a set and assign it to a variable
sets = {1, 2, 3}

# Find the length of the set
print('length of sets is', len(sets))

# Add a new element
sets.add(4)
print(sets)

# Remove an element
sets.remove(4)
print(sets)

# Check whether a element is in the set
if 1 in sets:
    print('1 in sets')

# Iterate over elements, printing each one out
for element in sets:
    print('element in sets is', element)


'''NUMBERS'''

# Add / subtract / multiply 2 numbers
number1 = 1
number2 = 2

add = number1 + number2
subtract = number1 - number2
multiply = number1 * number2

#############!!!!!!!!!!!!!!!!!
# Divide two numbers using normal (float) division
divide1 = 1.0 / 2.0
print(divide1) # 0.5

#############!!!!!!!!!!!!!!!!!
# Divide two numbers using integer division
divide2 = 3 // 2
print(divide2) # 1

# Find the modulo (remainder) of two numbers
remainder = 5 % 3
print('remainder is ', remainder)

# Check whether a number is even/odd
# % 
# NOT //
number = 4
if number % 2 == 0:
    print(f'number is {number}, even')

number = 3
if  number % 2 != 0:
    print(f'number is {number}, odd')

# Round a float down to an int
print(round(4.2))

'''FUNCTIONS'''

# Write a function that takes no arguments and call it
def add():
    print('function is add')
add()

# Write a function that takes one or more arguments and call it
def add(n1, n2):
    print(f'function is add, {n1}, {n2}')
add(1, 2)

# Write a function that returns a value. Call the function and store the return value in a variable
def add(n1, n2):
    return n1 + n2
result = add(1, 2)
print(f"{result = }")


'''LOOPS'''

# Write a while loop
i = 0
while i < 3:
    print(i)
    i += 1


# Write a for loop that loops a set number of times (e.g. 10 times)
for i in range(10):
    print(f'loops times is {i}')

'''CONDITIONALS'''

# Write an if/elif/else statement
n1 = 3
n2 = 5
if n1 > n2:
    print('bigger')
elif n1< n2:
    print('less')
else:
    print('equal')


# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=
if 1 == 1:
    print('equal')
if 2 != 1:
    print('NOT equal')
if 1 < 1:
    print('less')
if 2 > 1:
    print('more')
if 1 <= 1:
    print('less')
if 2 >= 1:
    print('more')

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable
nested_lists = [[4, 5, 6], [1, 2, 3]]

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second
for elements in nested_lists:
    for element in elements:
        print(element)

print(nested_lists[0])  # row 0 
print(nested_lists[0][0])  # row 0 column 0

# Iterate through the nested data structure using range
for i in range(len(nested_lists)):
    for j in range(len(nested_lists[i])):
        print(nested_lists[i][j])

# Iterate through the nested data structure without using range 
for elements in nested_lists:
    for element in elements:
        print(element)

'''REMINDER'''

# You're doing great and you got this!
