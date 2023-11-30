def display_students(student_dict):
    print(f"{str(student_dict)}")

def add_student(student_dict):
    name, grade = input("Enter the name and grade of the new student (comma-separated): ").split(", ")
    student_dict[name] = grade

def delete_student(student_dict):
    name = input("Enter the name of the student to delete: ")
    student_dict.pop(name, None)

names = {input("Enter student name: "): input("Enter grade: ") for _ in range(int(input("Enter how many student names you want to enter: ")))}

print("Initial Dictionary:")
display_students(names)

while True:
    print("\nSelect a Command: Add[A] / Delete[D] / Exit[E]")
    choice = input().lower()

    if choice == 'a':
        add_student(names)
    elif choice == 'd':
        delete_student(names)
    elif choice == 'e':
        break
    else:
        print("Invalid choice. Please enter 'A', 'D', or 'E'.")

print("\nFinal Dictionary:")
display_students(names)