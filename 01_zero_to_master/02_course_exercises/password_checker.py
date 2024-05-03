username = input("Please enter your username: ")
password = input("Please enter your password: ")

password_length = len(password)
hidden_password = '*' * password_length

print(f"Hi {username}, your password {
      hidden_password} has {password_length} characters")
