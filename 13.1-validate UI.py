username = input("Enter your username: ")

char = len(username)
spaces = username.count(" ")
digits = username.isdigit()
if char > 11:
    print("Too many characters!")
elif spaces > 0:
    print("There are spaces in your username!")
elif digits == True:
    print("There are digits in your username!")
else:
    print(f"Thank you for signing in {username}!")