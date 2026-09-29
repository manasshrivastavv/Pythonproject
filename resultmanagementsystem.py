students = []


def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 75:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 40:
        return "C"
    else:
        return "Fail"


def add_student():
    print("\n----- Add Student -----")
    name = input("Enter Name: ")

    eng = int(input("English Marks: "))
    math = int(input("Math Marks: "))
    sci = int(input("Science Marks: "))

    total = eng + math + sci
    per = total / 3
    g = grade(per)

    students.append({
        "name": name,
        "eng": eng,
        "math": math,
        "sci": sci,
        "total": total,
        "per": per,
        "grade": g
    })

    print("Student Added Successfully!")


def display():
    print("\n----- Student Records -----")

    if len(students) == 0:
        print("No Records Found")
    else:
        for s in students:
            print("---------------------------")
            print("Name :", s["name"])
            print("English :", s["eng"])
            print("Math :", s["math"])
            print("Science :", s["sci"])
            print("Total :", s["total"])
            print("Percentage :", round(s["per"],2))
            print("Grade :", s["grade"])


def search():
    name = input("Enter Student Name: ")

    for s in students:
        if s["name"].lower() == name.lower():
            print(s)
            return

    print("Student Not Found")


def update():
    name = input("Enter Student Name: ")

    for s in students:
        if s["name"].lower() == name.lower():

            s["eng"] = int(input("New English Marks: "))
            s["math"] = int(input("New Math Marks: "))
            s["sci"] = int(input("New Science Marks: "))

            s["total"] = s["eng"] + s["math"] + s["sci"]
            s["per"] = s["total"] / 3
            s["grade"] = grade(s["per"])

            print("Record Updated")
            return

    print("Student Not Found")


def save():
    file = open("student_results.txt","w")

    for s in students:
        file.write(str(s) + "\n")

    file.close()
    print("Data Saved Successfully")


def load():
    file = open("student_results.txt","r")

    print("\nSaved Records")
    print(file.read())

    file.close()


while True:

    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Save Result")
    print("6. Load Result")
    print("7. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        add_student()

    elif ch == "2":
        display()

    elif ch == "3":
        search()

    elif ch == "4":
        update()

    elif ch == "5":
        save()

    elif ch == "6":
        load()

    elif ch == "7":
        print("----Thank You For Using REsult Managementsystem----")
        break

    else:
        print("Invalid Choice")