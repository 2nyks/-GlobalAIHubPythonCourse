user = {"globalaihub": 123456}

username = str(input("Please enter a username: "))
password = int(input("Please enter a password: "))

User = {username: password}

if user == User:
    print("Your login is successfull.")
else:
    print("You entered an incorrect username or password.")