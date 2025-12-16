import array as myarray

abc = myarray.array('d', [2.5, 4.9, 6.7])
print(abc[1])

# The array index starts with 0. You can also access the last element of an array using the -1 index.
import array as myarray

abc = myarray.array('d', [2.5, 4.9, 6.7])
print("Array first element is:", abc[0])
print("Array last element is:", abc[-1])
abc.insert(1, 6.9)
print(abc)

# How to modify elements?
import array as myarr

print("*****Array****")
a = myarr.array('b', [3, 6, 4, 8, 10, 12, 14, 16, 18, 20])
a[0] = 99
print("Modified array:")
print(a)

# concatenation operations on arrays
import array as myarr

first = myarr.array('b', [4, 6, 8])
second = myarr.array('b', [9, 12, 15])
numbers = myarr.array('b')
numbers = first + second
print("Concatenation of two arrays:")
print(numbers)

# pop an element from Array
import array as myarr
first = myarr.array('b', [20, 25, 30])
first.pop(2)
print("Popped element:")
print(first)

# del’ statement of Python.
import array as myarr
no = myarr.array('b', [10, 4, 5, 5, 7])
del no[4]
print(no)

# delete elements - meaning values directly instead of index
no.remove(10)
print("removed element:")
print(no)

# Search and get the index of a value
import array as myarray
number = myarray.array('b', [2, 3, 4, 5, 6])
print("Index of 3:")
print(number.index(3))

# Reverse an Array
number.reverse()
print("Reverse of an array:")
print(number)

# Convert array to Unicode:
from array import array
p = array('u',[u'\u0050',u'\u0059',u'\u0054',u'\u0048',u'\u004F',u'\u004E'])
print(p)
Unicode = p.tounicode()
print("Unicode of an array:")
print(Unicode)


# Count the occurrence of a Value
import array as myarr
number = myarr.array('b', [2, 3, 5, 4,3,3,3])
print(number.count(3))


# *********Summary********
    # An array is a common type of data structure wherein all elements must be of the same data type.
    # Python programming, an array, can be handled by the “array” module.
    # Python arrays are used when you need to use many variables which are of the same type.
    # In Python, array elements are accessed via indices.
    # Array elements can be inserted using an array.insert(i,x) syntax.
    # In Python, arrays are mutable.
    # In Python, a developer can use pop() method to pop and element from Python array.
    # Python array can be converted to Unicode. To fulfill this need, the array must be a type ‘u’; otherwise, you will get “ValueError”.
    # Python arrays are different from lists.
    # You can access any array item by using its index.
    # The array module of Python has separate functions for performing array operations.