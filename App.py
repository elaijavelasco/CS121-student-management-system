import csv

student_fields = ['Roll', 'Name', 'ID No.', 'Program', 'Year']
student_database = 'students.csv'


def show_menu():
    print("Student Database Management System")
    while True:
        print ("Main Menu: ")
        print("1. Add New Student")
        print("2. View Student Information")
        print("3. Search Student Information")
        print("4. Update Student Information")
        print("5. Delete Student Information")
        print("6. Quit")

        choice = ""
        try: 
            choice = int(input("Enter your choice: "))
        except ValueError:
            print ("Invalid Input! Enter choice from the ff. [1,2,3,4,5, or 6].")

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print ("Thank you for using the application!")

        else:
            print ("Invalid Input! Try again...")
            break


def add_student():
    print("Add Student Information")
    global student_fields
    global student_database


    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully! ")
    input("Press any key to continue...")
    return


def view_students():
    global student_fields
    global student_database

    print("Student Records")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end="\t\t|")
        print("\n-----------------------------------------------------------------\n")

        for row in reader:
            for item in row:
                print(item, end="\t   |")
            print("\n")

    input("Press any key to continue...")


def search_student():
    global student_fields
    global student_database

    print("Search Student Information")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("Student: ")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("SR-CODE: ", row[2])
                    print("Program: ", row[3])
                    print("Year: ", row[4])
                    break
        else:
            print("Roll No. not found in our database.")
    input("Press any key to continue...")


def update_student():
    global student_fields
    global student_database

    print("Update Student Information")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database.")

    input("Press any key to continue...")


def delete_student():
    global student_fields
    global student_database

    print("Delete Student Information")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully!")
    else:
        print("Roll No. not found in our database.")

    input("Press any key to continue...")

show_menu()
