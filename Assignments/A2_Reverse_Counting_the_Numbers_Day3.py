## Reverse Counting (Print numbers from 10 to 1)
m = int(input("Enter Largest Number:"))
n = int(input("Enter Smaller Number:"))
for i in range(m, n, -1):
    print(i)
    