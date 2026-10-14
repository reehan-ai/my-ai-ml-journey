# Python Programming Handbook - Chapter 04

## Lists and Tuples

Python lists are containers to store a set of values of any data type.

**Example:**
`friends = ["apple", "akash", "rohan", 7, false]`

*   `"apple"`, `"akash"`, `"rohan"` -> `str()`
*   `7` -> `int()`
*   `false` -> `bool()`
*   Lists can store values of any datatype.

### List Indexing

A list can be indexed just like a string.

```python
l1 = [7, 9, "harry"]
l1[0] # 7
l1[1] # 9
l1[2] # "harry"

l1[0:2] # [7, 9] (a list slicing)
List Methods
Consider the following list:

python
l1 = [1, 8, 7, 2, 21, 15]
l1.sort(): updates the list to [1, 2, 7, 8, 15, 21]

l1.reverse(): updates the list to [15, 21, 2, 7, 8, 1]

l1.append(8): adds 8 at the end of the list

l1.insert(3, 8): This will add 8 at index 3

l1.pop(2): Will delete element at index 2 and return its value.

l1.remove(21): Will remove 21 from the list.

Tuples in Python
A tuple is an immutable data type in Python.

python
a = ()       # empty tuple
a = (1,)     # tuple with only one element needs a comma
a = (1, 7, 2) # tuple with more than one element
Tuple Methods
Consider the following tuple:

python
a = (1, 7, 2)
a.count(1): will return number of times 1 occurs in a.

a.index(1): will return the index of first occurrence of 1 in a.