from Admin import Admin_Menu
import csv
import sys

class Student:
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

            if self.choice == 1:
                Admin_Menu.viewRecords(self)

            elif self.choice == 2:
                Admin_Menu.searchRecord(self)

            elif self.choice == 3:
                print("\n\n",71*'-')
                print("\n\t\t** Thank you for using the application! **")
                print("\n",71*'-',"\n\n")
                sys.exit()
            else:
                break
