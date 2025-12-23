print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if input("Are you sure? (y/n): ") == "y":
        print("Enjoy the ride!")
    else:
        print("Okay, see you later!")
else:
    print("You can't ride the rollercoaster")

# logical Operators: and, or, not ex: age >= 18 and gender == "male", ex: age >= 18 or gender == "male", ex: age >= 18 and not gender == "male"


# % modular Operator
#  10 / 3 = 3.3333333333333335 with 1 has reminder
#
# number_to_check = print(input("What is the number you want to check Modular for?"))
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
