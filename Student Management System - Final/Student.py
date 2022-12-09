from Admin import Admin
import sys

class Student:
    def studentMenu(self):
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
                Admin.viewRecords(self)

            elif self.choice == 2:
                Admin.searchRecord(self)

            elif self.choice == 3:
                print("\n\n",71*'-')
                print("\n\t\t** Thank you for using the application! **")
                print("\n",71*'-',"\n\n")
                sys.exit()
            else:
                break

