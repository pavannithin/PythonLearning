from string import capwords

studentsMarks = [156, 78, 456, 877, 146, 765, 988, 556, 778]
max_score = 0
for student in studentsMarks:
    if student > max_score:
        max_score = student
print(f"The highest score is: {max_score}")

# Range
# example 1
for each in range(1, 10, 2):
    print(each)
# example 2
score = 0
for each in range(1, 10, 2):
    print(each)
    if each == max_score:
        score += 1
        print(f"Your score is: {score}")
    elif each == max_score:
        score += 2
        print(f"Your score is: {score}")
    else:
        print("No score change")

# PROBLEM STATEMENT
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
#
#
#
# Your program should print each number from 1 to 100 in turn and include number 100.
#
#
#
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
#
#
#
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#
#
#
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
#
#
#
# e.g. it might start off like this:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc

# Answer:
for each in range(1, 101):
    if (each % 3 == 0 and each % 5 == 0):
        print("FizzBuzz")
    elif (each % 3 == 0):
        print("Fizz")
    elif (each % 5 == 0):
        print("Buzz")
    else:
        print(each)
import random
# Password Generator
smallLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
capLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

print('welcome to password generator ')
nr_letters = int(input('How many letters would you like in your password?\n'))
nr_symbols = int(input('How many symbols would you like?\n'))
nr_numbers = int(input('How many numbers would you like?\n'))

# Easy level
password = ""
for letter in range(0, nr_letters):
    password += random.choice(smallLetters)

for symbol in range(0, nr_symbols):
    password += random.choice(capLetters)

for eachNumber in range(0, nr_numbers):
    password += random.choice(numbers)

print("password = ", password)

# Hard Level
password_list = []
for letter in range(0, nr_letters):
    password_list.append(random.choice(smallLetters))

for symbol in range(0, nr_symbols):
    password_list.append( random.choice(capLetters))

for eachNumber in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
print("password = ", password_list)
random.shuffle(password_list)
print("password shuffle = ", password_list)
finalHardPassword = ""
for letter in  password_list:
    finalHardPassword += letter
print("finalHardPassword= ", finalHardPassword)
