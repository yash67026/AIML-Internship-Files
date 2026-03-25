# Keep asking user to enter numbers and calculate the sum. Stop only when the User Enters 0:
total = 0
print("Welcome to Summing Game, Enter 0 to stop the Game: ")
while True:
    num = int(input("Enter the number: "))
    if num == 0:
        break
    total += num

print("Sum =", total)