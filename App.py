import csv
import sys

student_fields = ['Roll', 'Name', 'ID No.', 'Program', 'Year']
student_database = 'students.csv'


def showMenu():
    global student_fields
    global student_database

    print("\n\t\t------------------------------------------------")
    print("\n\t\t\t  **Student Management System**")
    print("\n\t\t------------------------------------------------")
    while True:
        print ("\n\t\tMain Menu:\n")
        print("\t\t\t(1) Add New Student")
        print("\t\t\t(2) View Student Information")
        print("\t\t\t(3) Search Student Information")
        print("\t\t\t(4) Update Student Information")
        print("\t\t\t(5) Delete Student Information")
        print("\t\t\t(6) Quit Application")

        choice = ""
        try:
            choice = int(input("\n\t\tEnter your choice: "))
                
        except ValueError:
            print ("\n\t\tInvalid Input! Choice should be a number.")
            response = (input("\n\t\tTry again? [y/n]: "))
            while response == 'y':
                choice = int(input("\n\t\tEnter your choice: "))
                break

        if choice == 1:
            addStudent()

        elif choice == 2:
            viewStudents()

        elif choice == 3:
            searchStudent()

        elif choice == 4:
            updateStudent()

        elif choice == 5:
            deleteStudent()

        elif choice == 6:
            input("Closing Program..... \nPlease press any key to continue\n")
            print("\n\t\t------------------------------------------------")
            print ("\n\t\t    **Thank you for using the application!**\n")
            print("\t\t------------------------------------------------\n\n\n")
            sys.exit()
        else:
            break

def addStudent():
    print("\n\t\t\tAdd Student Information\n")
    global student_fields
    global student_database


    student_data = []
    for field in student_fields:
        value = input("\t\t\tEnter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully! ")
    input("Press any key to continue...")
    return


def viewStudents():
    global student_fields
    global student_database

    print("\n\t\t\tStudent Records\n")

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_fields:
            print(x, end="\t\t|")
        print("\n-----------------------------------------------------------------\n")

        for row in reader:
            for item in row:
                print(item, end="\t   |")
            print("\n")

    input("\n\t\tPress any key to continue...")


def searchStudent():
    global student_fields
    global student_database

    print("\n\t\t\tSearch Student Information\n")
    roll = input("\t\t\tEnter roll no. to search: ")
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
            print("\n\t\t\tRoll No. not found in our database.\n")
    input("\t\tPress any key to continue...")


def updateStudent():
    global student_fields
    global student_database

    print("\n\t\t\tUpdate Student Information\n")
    roll = input("\t\t\tEnter roll no. to update: ")
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
        print("\n\t\t\tRoll No. not found in our database.\n")

    input("\t\tPress any key to continue...")


def deleteStudent():
    global student_fields
    global student_database

    print("\n\t\t\t ***Delete Student Information***\n")
    roll = input("\t\t\tEnter roll no. to delete: ")
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
        print("\n\t\t\tRoll No. not found in our database.\n")

    input("\t\tPress any key to continue...")

showMenu()
