# Student Data Manager

students = {}   # Dictionary to store student data

n = 5  # Number of students

# Taking input
for i in range(n):
    print(f"\nEnter details of Student {i+1}")
    name = input("Name: ")
    marks = float(input("Marks: "))

    students[name] = marks

# Display students
print("\n--- Student Marks ---")
for name, marks in students.items():
    print(f"{name} : {marks}")

# Finding topper
topper = max(students, key=students.get)
print(f"\nTopper: {topper} with {students[topper]} marks")

# Class average
average = sum(students.values()) / n
print(f"Class Average: {average:.2f}")

# Assigning grades
print("\n--- Grades ---")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"{name} : Grade {grade}")