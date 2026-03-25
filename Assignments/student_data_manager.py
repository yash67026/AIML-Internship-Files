# assigning grades
def assign_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 55:
        return "C"
    else:
        return "D"


students = {}
total_marks = 0
topper = ""
highest_marks = 0

# Taking input for 5 
for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks

print("\n--- Student Details ---")
for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"{name} → Marks: {marks}, Grade: {grade}")

    total_marks += marks
    if marks > highest_marks:
        highest_marks = marks
        topper = name

average = total_marks / len(students)

print("\n--- Results ---")
print("Topper:", topper, "with", highest_marks, "marks")
print("Class Average:", average)