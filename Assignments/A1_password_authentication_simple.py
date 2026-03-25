# Program for Simple Password Authentication

actual_username = "Yashwanth H"
actual_password = "yashu123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == actual_username and password == actual_password:
    print("Login success!")
    print("Welcome")
else:
    print("Invalid username or password")
