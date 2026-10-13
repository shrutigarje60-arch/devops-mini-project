students = []

def add_student():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    students.append({
        "name": name,
        "roll": roll
    })

    print("Student Added Successfully!")

def view_students():
    print("\nStudent Records:")

    for student in students:
        print(student["roll"], student["name"])

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
