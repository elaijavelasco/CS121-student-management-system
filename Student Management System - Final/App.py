from Student import Student
from Admin import Admin
import sys

#main app menu
class App:
    def userMode(self):
        print("\n",71*'-')
        print("\n\t\t\tStudent Management System")
        print("\n",71*'-')  
        print ("\n\t\t\tChoose User Mode: \n")
        print ("\t\t\t    1 - Admin Mode")
        print ("\t\t\t    2 - Student Mode")
        print ("\t\t\t    3 - Quit Menu")      

        option = ""
        try:
            option = int(input("\n\t\t\tWhat user are you? "))
        except ValueError:
            print("\n\t\tInvalid Entry! Input should be a number.")
            App.back(self)
                
        if option == 1:
            print("\n",71*'=')
            print("\n\t\t\t   >> ADMIN MODE <<")
            Admin.login(self)
                       
        elif option == 2:
            print("\n",71*'=')
            print("\n\t\t\t  >> STUDENT MODE <<")
            Student.studentMenu(self)
        
        elif option == 3:
            print("\n\n\n",73*'-')
            print("\n\t\t\tYou've exited the application!")
            print("\n",73*'-')
            sys.exit()

        else:
            print("\n\t  Invalid Entry! Input should be from the option.\n")
            App.back(self)

    def back(self):
        App.userMode(self)