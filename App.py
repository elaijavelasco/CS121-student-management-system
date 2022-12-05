import csv
import sys

#global variables
student_fields = ['Roll', 'Full Name', 'ID Number', 'Program', 'Year Level']
student_database = 'students.csv'

#function to display menu
def showMenu():
    print("\n",71*'-')
    print("\n\t\t\tStudent Management System")
    print("\n",71*'-')

    while True:
        print ("\n\t\tMain Menu:\n")
        print("\t\t\t(1) Add New Student")
        print("\t\t\t(2) View Student Records")
        print("\t\t\t(3) Search Student Record")
        print("\t\t\t(4) Update Student Record")
        print("\t\t\t(5) Delete Student Record")
        print("\t\t\t(6) Quit Application")

    #input choice
        choice = ""
        try:
            choice = int(input("\n\t\tWhat do you want to do? "))
    #handle input error      
        except ValueError:
            print ("\n\t\tInvalid Entry! Input should be a number.")
            response = (input("\n\t\tTry again? [y/n]: "))
            print("\n\n")

            while response == 'y':
                choice = int(input("\n\t\tEnter your choice: "))
                break

        if choice == 1:
            addRecord()

        elif choice == 2:
            viewRecords()

        elif choice == 3:
            searchRecord()

        elif choice == 4:
            updateRecord()

        elif choice == 5:
            deleteRecord()

        elif choice == 6:
            print("\n\n",71*'-')
            print("\n\t\t** Thank you for using the application! **")
            print("\n",71*'-',"\n\n")
            sys.exit()
        else:
            break

#function to add student record
def addRecord():
    print("\n\n\t\t\t** Add Student Record **\n")
    global student_fields
    global student_database

    student_data = []

    print("\n",71*'=')
    print("\n\t\t\t >> Fill-in Information << \n")

    for field in student_fields:
        value = input("\t\t\tEnter " + field + ": ")
    #add inputted value to the list
        student_data.append(value)
    print("\n",71*'=')

    #method to open database
    with open(student_database, "a", encoding="utf-8") as f:
    #insert the data to csv file
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("\n\n\t\t\t** Data saved successfully! **")
    input("\n\t\t\tPress any key to continue...")
    print("\n")
    return

#function to view student records
def viewRecords():
    global student_fields
    global student_database

    print("\n\n\t\t\t ** Student Records **")
    print("\n",71*'-')

    #method to access the student database
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        #to access all fields & values
        for x in student_fields:
            print(x, end="\t|   ")
        print("\n",71*'-')

        for row in reader:
            for item in row:
                print(item, end="\t|   ")
            print("\n")
    
    input("\t\t\tPress any key to continue...")
    print("\n")

#function to search student record
def searchRecord():
    global student_fields
    global student_database

    print("\n\n\t\t\t** Search Student Record **\n")
    roll = input("\t\t\tEnter roll number to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            #returns the object with matching roll number
            if len(row) > 0:
                if roll == row[0]:
                    print("\n",71*'=')
                    print("\n\t\t\t   >> Student Record << \n")
                    print("\t\t\t Roll: ", row[0])
                    print("\t\t\t Full Name: ", row[1])
                    print("\t\t\t ID Number: ", row[2])
                    print("\t\t\t Program: ", row[3])
                    print("\t\t\t Year Level: ", row[4])
                    print("\n",71*'=')
                    break
    #if no record is found
        else:
            print("\n\n\t\t** Roll number not found in our database! **")
    input("\n\n\t\t\tPress any key to continue...")
    print("\n")

#function to update student records
def updateRecord():
    global student_fields
    global student_database

    print("\n\n\t\t\t** Update Student Information **\n")
    roll = input("\t\t\tEnter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
    #to access the rows
        for row in reader:
            #to access the roll 
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("\n\t\t\tStudent found at index [",index_student, "] ")
                    print("\n",71*'=')
                    print("\n\t\t\t>> Fill-in New Record << \n")
                    student_data = []
                    for field in student_fields:
                        value = input("\t\t\tEnter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                    print("\n",71*'=')
                    print("\n\n\t\t\t** Data saved successfully! **")
                    
                    print
                else:
                    updated_data.append(row)
                counter += 1
                
    #checks if the student record is found or not
    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("\n\t\t** Roll number not found in our database! **\n")

    input("\n\t\t\tPress any key to continue...")
    print("\n")

#function to delete student records
def deleteRecord():
    global student_fields
    global student_database

    print("\n\n\t\t\t ***Delete Student Information***\n")
    roll = input("\t\t\tEnter roll number to delete: ")
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

#checks if the student record is found or not
    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("\n",71*'=')
        print("\n\t\t\tRoll no. ", roll, "deleted successfully!")
        print("\n",71*'=')

#if no record found
    else:
        print("\n\t\t** Roll number not found in our database! **\n")

    input("\n\n\t\t\tPress any key to continue...")
    print("\n")

showMenu()