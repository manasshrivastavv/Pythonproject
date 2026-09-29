print("----Welcome To Student Management Program----")

students = []

def Intro():
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Exit")

def add():
    print("\n----Add Student----")
    name = input("Enter Name: ")
    
    roll_input = input("Enter Roll No.: ")
    # Checks if the input is a valid number using an if-statement
    if roll_input.isdigit():
        roll = int(roll_input)
    else:
        print("Invalid roll number! Student not added.")
        return

    branch = input("Enter Branch: ")
    
    phone_input = input("Enter Phone Number: ")
    if phone_input.isdigit():
        phone = int(phone_input)
    else:
        print("Invalid phone number! Student not added.")
        return

    student = {
        "name": name,
        "roll": roll,
        "branch": branch,
        "phone": phone
    }

    students.append(student)
    print("Student Added Successfully!")

def view():
    print("\n----Student List----")
    if len(students) == 0:
        print("No Students Found!")
        return

    for student in students:
        print(f"Roll No: {student['roll']} | Name: {student['name']} | Branch: {student['branch']} | Phone: {student['phone']}")
        print("-" * 30)

def search():
    print("\n----Search Student----")
    roll_input = input("Enter Roll No to Search: ")
    
    if roll_input.isdigit() == False:
        print("Invalid input! Please enter a number.")
        return
        
    roll = int(roll_input)
    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print(f"Name: {student['name']}\nBranch: {student['branch']}\nPhone: {student['phone']}")
            return

    print("Student Not Found!")
def delete():
    print("\n----Delete Student----")
    roll_input = input("Enter Roll No to Delete: ")
    
    if roll_input.isdigit() == False:
        print("Invalid input! Please enter a number.")
        return
        
    roll = int(roll_input)
    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

# --- Main Program Loop ---
while True:
    Intro()
    
    choice_input = input("Enter Your Choice (1 - 5): ")
    
    if choice_input.isdigit():
        choice = int(choice_input)
    else:
        print("Please enter a valid menu number.")
        continue

    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        delete()
    elif choice == 4:
        search()
    elif choice == 5:
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1 to 5.")
