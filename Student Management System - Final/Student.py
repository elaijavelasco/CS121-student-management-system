import csv
import sys

student_fields = ['Roll', 'Full Name', 'ID Number', 'Program', 'Year Level']
student_database = 'students.csv'

#function to display menu
def showMenu():
    print("\n",71*'-')
    print("\n\t\t\tStudent Menu")
    print("\n",71*'-')

    while True:
        print ("\n\t\tStudent Menu:\n")
        print("\t\t\t(1) View Student Records")
        print("\t\t\t(2) Search Student Record")
        print("\t\t\t(3) Quit Application")

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
            viewRecords()

        elif choice == 2:
            searchRecord()

   
        elif choice == 3:
            print("\n\n",71*'-')
            print("\n\t\t** Thank you for using the application! **")
            print("\n",71*'-',"\n\n")
            sys.exit()
        else:
            break

#function to view student records
def viewRecords():
    global student_fields
    global student_database

    print("\n\n\t\t\t ** Student View **")
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