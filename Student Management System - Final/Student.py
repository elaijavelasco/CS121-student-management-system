from Admin import Admin
import sys

class Student:
    def studentMenu(self):
        while True:
            print ("\n\t\tStudent Menu:\n")
            print("\t\t\t(1) View Records")
            print("\t\t\t(2) Search Record")
            print("\t\t\t(3) Sort Records")
            print("\t\t\t(4) Quit Application")

            self.choice = ""
            try:
                self.choice = int(input("\n\t\tWhat do you want to do? "))
            except ValueError:
                print ("\n\t\tInvalid Entry! Input should be a number.")
                self.goToMenu()

            if self.choice == 1:
                print("\n\n\t\t\t ** Students Records **")
                Admin.viewRecords(self)

            elif self.choice == 2:
                print("\n\n\t\t\t   ** Find Record **")
                Admin.searchRecord(self)
            
            elif self.choice == 3:
                print("\n\n\t\t\t ** Sorted Record **")
                Admin.sortRecords(self)

            elif self.choice == 4:
                print("\n\n",71*'-')
                print("\n\t\t** Thank you for using the application! **")
                print("\n",71*'-',"\n\n")
                sys.exit()
            else:
                break
        
    def goToMenu(self):
        back = input("Type 'z' to be back on Menu: ")
        if back == 'z':
            self.studentMenu()
        else:
            sys.exit()

