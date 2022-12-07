from Student import Student
from Admin import Admin
import sys

class App:
    def userMode(self):
        print ("User Mode: ")
        print ("1 - Admin")
        print ("2 - Student")
        print ("3 - Quit")        

        option = ""
        try:
            
            option = int(input("\nWhat user are you? "))
        except ValueError:
            print("\nInvalid Entry!")
        except Exception as E:
            print(E)
        
            response = (input("\nTry again? [y/n]: "))
            if response == 'y':
                option = int(input("\nWhat user are you? "))
            else:
                sys.exit()
                return
                
        if option == 1:
            Admin.login(self)
                
        elif option == 2:
            Student.studentMenu(self)
        
        elif option == 3:
            sys.exit()
        else:
            print("\nInvalid Entry! Input should be from the option.\n")
            return self.userMode()
  
def runApp():
    app = App()
    app.userMode()
    
runApp()



            

