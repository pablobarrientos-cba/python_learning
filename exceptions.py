num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

# try:
#     print("Normal execution")
# except:
#     print("Exception Thrown")
# else:
#     print("Executes after successful try")
# finally:
#     print("Executes no matter what")

try:
    result = num1 / num2
    print(f"{num1}/{num2} =", result)
except ZeroDivisionError as zero_div:
    print(zero_div)
else:
    print("No exception thrown")
finally:
    print("Executing Finally")
