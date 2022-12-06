import csv
import sys

class Student_Database:
    def __init__(self):
        self.admin_fields = ['Username', 'Password']
        self.admin_database = 'admin.csv'

class Student_Menu(Student_Database):
    def __init__(self):
        super().__init__(self)

    def studentMenu(self):
        print("\n",71*'-')
        print("\n\t\t\tStudent Menu")
        print("\n",71*'-')

        while True:
            print ("\n\t\tStudent Menu:\n")
            print("\t\t\t(1) View Student Records")
            print("\t\t\t(2) Search Student Record")
            print("\t\t\t(3) Quit Application")

            self.choice = ""
            try:
                self.choice = int(input("\nWhat do you want to do? "))
            except ValueError:
                print ("Invalid Entry!")
                self.response = (input("\nTry again? [y/n]: "))

                while self.response == 'y':
                    self.choice = int(input("Enter your choice: "))
                    break

            if choice == 1:
                self.viewRecords()

            elif choice == 2:
                self.searchRecord()

            elif choice == 3:
                print("\n\n",71*'-')
                print("\n\t\t** Thank you for using the application! **")
                print("\n",71*'-',"\n\n")
                sys.exit()
            else:
                break

