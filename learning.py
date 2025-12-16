from operator import truediv

print("hello world")

# Declare a variable and initialize it
f = 0
print(f)
# re-declaring the variable works
f = 'guru99'
print(f)

# Python String Concatenation and Variable
a = "Guru"
b = 99
print(a + str(b))

# **# Python Variable Types: Local & Global **

# Declare a variable and initialize it
f = 101
print(f)


# Global vs. local variables in functions
def someFunction():
    # global f
    f = 'I am learning Python'
    print(f)


someFunction()
print(f)

# How to Delete a Variable?

f = 11;
print(f)
del f
# print(f)


# **************Python Types**************
# Binary Types
print("****Binary Types****")
# bytes
k = b"any_Char"
print("bytes " + k.decode())
# bytes Array
y = bytearray(10)
print("bytearray = " + y.decode())
# memoryview
c = memoryview(bytes(10))
print("memoryview = ", c)

# Text Types
print("****Text Types****")
a = "any_Char"
print("String = " + a)
a = """any_Char
second line
third line
fourth line"""
print("Multiple line String = " + a)
b = '''any_Char
second line
third line
fourth line'''
print("Multiple line String = " + b)

print("Retrieving a Character from a String: ")
a = "String"
print("char at index 0: " + a[0])  # OP: S
for a in "String":
    print(a)

# Boolean types
print("****Boolean types****")
a = True
b = False

c = 10 > 5
print(c)  # OP: True because of integer comparision
d = 23.56
e = 78.12
print(d == e)
print("case sensitivity: ")  # OP: False because of float point comparision
print("String" == "string")  # OP: False because of case sensitivity

print("****type Function****")
# Type()
# Type of k is : <class 'bytes'>
a = 1
print(type(a))
b = 12.21
print(type(b))
c = complex(7, 5)
print(type(c))
d = "String"
print(type(d))
e = 10 > 5
print(type(e))
f = None
print(type(f))

print("****Numeric Types****")
# int, float and complex are three data types in Python which handle numbers.
print("\t****Complex Type****")
a = 5 + 7j
print(a)
print(a.real)  # OP: 5
print(a.imag)  # OP: 7
# complex
a = complex(7)
print(a)
b = complex(7, 5)
print(b)

print("*****Tuples in Python*****")
tup1 = ('Robert', 'Carlos', '1965', 'Terminator 1995', 'Actor', 'Florida');
tup2 = (1, 2, 3, 4, 5, 6, 7);
print(tup1[0])  # OP: Robert
print(tup2[1:4])  # OP: (2,3,4)

x = ("Guru99", 20, "Education")  # tuple packing
(company, emp, profile) = x  # tuple unpacking
print(company)
print(emp)
print(profile)
# The comparison starts with a first element of each tuple. If they do not compare to =,< or > then it proceed to the second element and so on.

# It starts with comparing the first element from each of the tuples
a = (1, 4)
b = (5, 6)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

a = (5, 6)
b = (5, 4)
if a > b:
    print("a is bigger")
else:
    print("b is bigger")

print("*****Using tuples as keys in dictionaries*****")
a = {'x': 100, 'y': 200}
b = list(a.items())
print(b)
# Deleting Tuples
# Tuples are immutable and cannot be deleted. You cannot delete or remove items from a tuple. But deleting tuple entirely is possible by using the keyword
print("*****Slicing of Tuple*****")
x = ("a", "b", "c", "d", "e")
print(x[2:4])

print("***Dictionary***")
Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print(Dict['Tiffany'])

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
Boys = {'Tim': 18, 'Charlie': 12, 'Robert': 25}
Girls = {'Tiffany': 22}
studentX = Boys.copy()
studentY = Girls.copy()
print(studentX)
print(studentY)

# UPDATING DICTIONARY

Dict.update({'kpn': 100})
print(Dict)

# delete dictionary
del Dict['Tiffany']
print(Dict)

Dict = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
print("Students Name: %s" % Dict.items())

# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# Boys = {'Tim': 18,'Charlie':12,'Robert':25}
for key in Boys.keys():
    if key in Dict.keys():
        print(f'key {key} True')
    else:
        print(f'key {key} False')
print("sorting the dictionary:")
Students = Dict.keys()
Students = sorted(Students)
print(Students)
for S in Students:
    print(":".join((S, str(Dict[S]))))

print("length: %d" % len(Dict))
print(" variable Type: %s" % type(Dict))
# def cmp(a, b):
#     return (a > b) - (a < b)
# print(cmp(Boys, Girls))


print("****Logical Operators or Bitwise Operators****")
a = True
b = False
print(('a and b is', a and b))
print(('a or b is', a or b))
print(('not a is', not a))

print("*****Membership Operators******")
x = 4
y = 20
list = [1, 2, 3, 4, 5];
if (x in list):
    print("Line 1 - x is available in the given list")
else:
    print("Line 1 - x is not available in the given list")
if (y not in list):
    print("Line 2 - y is not available in the given list")
else:
    print("Line 2 - y is available in the given list")

print("*****Identity Operators******")
x = 20
y = 20
if (x is y):
    print("x & y  SAME identity")
y = 30
if (x is not y):
    print("x & y have DIFFERENT identity")

print("*****Operator Precedence******")
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v + w) * x / y;
print("Value of (v+w) * x/ y is ", z)

print("*********Not equal to operator**************")
A = 44
B = 284
C = 284
print(B != A)
print(B != C)

print("*********Overriding the __ne__() method**************")
class KPNExample:
    s_n = ''

    def __init__(self, name):
        self.s_n = name

    def __ne__(self, x):
        if type(x) != type(self):
            return True
        if self.s_n != x.s_n:
            return True
        else:
            return False
K1 = KPNExample('KPN')
K2 = KPNExample('KPN')
K3 = KPNExample('KPN2')
print(K1 != K2)
print(K2 != K3)
print(K1 != K3)