Strings
String is a data type in Python.

String is a sequence of characters enclosed in quotes.

We can primarily write a string in these three ways:

python
a = 'anything...'    # Single quoted string
b = "anything..."    # Double quoted string
c = '''anything...''' # Triple quoted string
String Slicing
A string in Python can be sliced for getting a part of the strings.

Consider the following string:
Name = "anything..." => Length = 5

Indexing:

Positive Index: Starts from 0 (left to right)

h = 0

a = 1

r = 2

r = 3

y = 4

Negative Index: Starts from -1 (right to left)

h = -5

a = -4

r = -3

r = -2

y = -1

The index in a string starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:

s = name[start:end]

First index included

Last index not included

Slicing with Skip Value
We can provide a skip value as a part of our slice like this:

python
word = "amazing"
word[1:6:2] # mzn
Other advanced slicing techniques:

python
word = "amazing"
word[-7:-1] # amazin
word[:7]    # amazing
word[0:]    # amazing
String Functions
Some commonly used functions to manipulate strings are:

1. len() returns the length of the string.

python
str = "anything..."
print(len(str)) # Output: 5
2. endswith() checks if a string ends with given text.

python
str = "anything..."
print(str.endswith("rry")) # Output: True
3. count() counts total occurrences of a character.

python
str = "anything..."
count = str.count("r")
print(count) # Output: 2
4. capitalize() capitalizes the first character.

python
str = "anything..."
capitalized = str.capitalize()
print(capitalized) # Output: Harry
String Functions Continued
5. find() returns the index of first occurrence.

python
str = "anything..."
index = str.find("rr")
print(index) # Output: 2
6. replace(old word, new word) replaces the old word with the new word in the string.

python
str = "anything..."
replaced = str.replace("r", "l")
print(replaced) # Output: hally
Escape Sequence Characters
Sequence of characters after backslash "" are called Escape Sequence characters. These characters represent one special character inside strings.

Examples:

\n : newline (moves cursor to line 2)

\t : Tab (moves cursor forward)

\' : single quote

\\ : backslash

etc.