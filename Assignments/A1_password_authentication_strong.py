print("Sign Up")
user_id = input("Create UserID: ")
password = input("Create Password: ")
confirm_password = input("Re-type Password: ")

if password != confirm_password:
    print("Passwords do not match. Please enter same password as entered above.")
else:
    print("\nSign Up Successful!\n")

    print("Sign In:")
    login_user = input("Enter UserID: ")
    login_password = input("Enter Password: ")

    if login_user == user_id and login_password == password:
        print(f"\nWelcome {user_id}...!")
    else:
        print("\nInvalid UserID or Password, please try again...!")


