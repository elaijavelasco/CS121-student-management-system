from Student import student_database

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin_Database:
    def __init__(self):
        self.admin_fields = ['Username', 'Password']
        self.admin_database = 'admin.csv'
 
class Admin_Menu(Admin_Database):
    def __init__(self):
        super().__init__(self)

    def adminMenu(self):
        print("\n",71*'-')
        print("\n\t\t\tAdmin Menu")
        print("\n",71*'-')

        while True:
            print("\n\t\tMain Menu:\n")
            print("\t\t\t(1) Add New Student")
            print("\t\t\t(2) View Student Records")
            print("\t\t\t(3) Search Student Record")
            print("\t\t\t(4) Update Student Record")
            print("\t\t\t(5) Delete Student Record")
            print("\t\t\t(6) Logout")

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
                self.login()

            if self.choice == 2:
                self.addRecord()

            if self.choice == 3:
                self.viewRecords()

            if self.choice == 4:
                self.searchRecord()
            
            if self.choice == 5:
                self.updateRecord()
            
            if self.choice == 6:
                self.deleteRecord()
            
            if self.choice == 7:
                self.logout()
            
            else:
                break
    
    def login (self):
        username = input("Enter username: ")
        if username not in self.admin_database:
            print ("Username or password invalid!")
            return
        
        password = input("Enter password: ")

        admin = self.admin_database[username]
        if admin.password != password:
            print("Username or password is invalid! ")
            return
        
        self.admin_logged_in = admin
        print ("Successfully Login!")

    def addRecord(self):
        pass

    def viewRecord(self):
        pass
    
    def searchRecord(self):
        pass
    
    def updateRecord(self):
        pass

    def deleteRecord(self):
        pass

    def admin_logout(self):
        pass
    
    def exit(self):
        pass