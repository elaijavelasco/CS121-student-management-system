from Student import Student_Menu
from Admin import Admin_Menu

class App:
    def userMode(self):
        print ("User Mode: ")
        print ("1 - Admin")
        print ("2 - Student")        

        option = ""
        try:
            option = int(input("What user are you? "))
        except ValueError:
            print("Invalid Entry!")
            response = (input("Try again? [y/n]: "))
                    
            while response == 'y':
                option = int(input("What user are you? "))
                break
                
        if option == 1:
            Admin_Menu.adminMenu(self)
                
        elif option == 2:
            Student_Menu.studentMenu(self)
    
def runApp():
    app = App()
    app.userMode()
    
runApp()



            

