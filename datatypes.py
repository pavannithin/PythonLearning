from pip._internal import operations

print("hello"[0])

# Type convesions
# String to int
print(int("123") + int("456"))
# int to string
print(str(123) + str(456))

# Mathematical operations
print(123 + 456)
print(123 - 456)
print(123 * 456)
print(123 / 456)
print(6 / 3)  # this will give a float type
print(6 // 3)  # this will give an Int type
print(2 ** 2)  # 2 to the power of 2 which is 4

print(3 * 3 + 3 / 3 - 3)  # this gives 7.0 because of the order of operations
print(3 * (3 + 3) / 3 - 3)  # this gives 3.0 because of the order of operations

# f-string
score = 0
height = 1.75
is_winning = True
print(f"Score: {score}, Height: {height:.2f}, Winning: {is_winning}")

# Tip Calculator
print("Tip Calculator:")
bill = float(input("Enter bill amount: "))
tip = int(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))
total_tip_amt = bill * tip / 100
total = bill + total_tip_amt
bill_per_person = total / people
print(f"Each person should pay: {bill_per_person:.2f}")
final_amt = round(total, 2)
print(f"Total bill: {final_amt}")

