from Student import*
from Admin import*

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
            self.login()
                
        elif option == 2:
            self.studentMenu()



            

