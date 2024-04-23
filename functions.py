# SYNTAX: def function(): 
# It does not support method overloading
# It can returns values, if not None is returned
# use print(result) if needed

def display_message_nop():
    print("This is a function")

def display_message(msg):
    print(msg)

display_message_nop()
display_message(2)
display_message("Hi there")