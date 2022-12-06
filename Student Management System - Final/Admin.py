class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Admin_Database:
    def __init__(self):
        self.admin_fields = ['Username', 'Password']
        self.admin_database = 'admin.csv'

class AdminLogin (Admin_Database):
    def __init__(self):
        super().__init__(self)
    
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