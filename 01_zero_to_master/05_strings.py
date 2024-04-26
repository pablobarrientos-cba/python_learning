# class str
# sting are immutable
print(type("Hello Pablo"))

double_quote = "Sample text"
single_quote = 'Sample text'

long_text = '''
this is a 
multi lineal
sample
'''

print(double_quote)
print(single_quote)
print(long_text)

# sting concatenation
first_name = "Pablo"
last_name = "Barrientos"
print(first_name + ' ' + last_name)

# string formatting
print(f"{first_name} {last_name}")

print(f"{first_name}\t{last_name}")
print(f"{first_name}\n{last_name}")

# escape characters
weather = "it\'s \"summer\" time"
print(weather)
print(weather.__add__(". Enjoy!"))