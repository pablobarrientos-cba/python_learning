to_minutes = 24 * 60
unit = "minutes"

print(f"20 days are {20 * to_minutes} {unit}")
print(f"30 days are {30 * to_minutes} {unit}")
print(f"50 days are {50 * to_minutes} {unit}")


def days_to_units(days):
    print("\n==== Calling the function ====")
    print(f"{days} days are {days * to_minutes} {unit}")
    print("===== Function Executed ======")


days_to_units(50)
days_to_units(27)

# Remarks:
# Function definition with reserved word def
# The function body is not enclosed by braces, but it is defined by the indentation.
# Always leave 2 lines before and after function definition
# Does not support overloading with additional params
# Variable scope similar to C#: Global, local
