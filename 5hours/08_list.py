# Enclosed by []
# List are mutable elements
# Zero indexed
# Basic operations: List elements, add item, remove item, access element by index

months = ["Jan", "Feb", "Mar"]
print(months)
print(months[0])  # first element
print(months[-1])  # last element

print(months.__contains__('Jan'))
months.pop(1)
print(months)

for month in months:
    print(f"=== {month} ===")
