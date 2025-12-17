print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    if input("Are you sure? (y/n): ") == "y":
        print("Enjoy the ride!")
    else:
        print("Okay, see you later!")
else:
    print("You can't ride the rollercoaster")

# % modular Operator
#  10 / 3 = 3.3333333333333335 with 1 has reminder
#
# number_to_check = print(input("What is the number you want to check Modular for?"))
# if number_to_check % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
