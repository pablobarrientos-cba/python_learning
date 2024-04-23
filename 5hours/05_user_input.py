def days_left(days):
    print(f"{days} days are left")


user_input = input("Enter the remaining days:\n ")
days_left(user_input)

num1 = input("Enter the first number: ")
num2 = input("Enter second number: ")

the_sum = num1 + num2
print(f'The sum is {the_sum}')

the_sum = float(num1) + int(num2)
print(f'The sum is {the_sum}')

# Remarks:
# Input is ALWAYS treated as STRINGS!!!
# So, if we need to process numbers we need to cast
