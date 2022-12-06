from Student import student_database
import csv

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
        print ("Successfully Logged in!")

    def addRecord(self):
        student_data = []

        print("\n",71*'=')
        print("\n\t\t\t >> Fill-in Information << \n")

        for field in self.student_fields:
            value = input("\t\t\tEnter " + field + ": ")
            student_data.append(value)
        print("\n",71*'=')

        with open(student_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([student_data])

        print("\n\n\t\t\t** Data saved successfully! **")
        self.exit()
        return
        
    def viewRecord(self):
        print("\n\n\t\t\t ** Student Records **")
        print("\n",71*'-')

        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in self.student_fields:
                print(x, end="\t|   ")
            print("\n",71*'-')

            for row in reader:
                for item in row:
                    print(item, end="\t|   ")
                print("\n")
            
            self.exit()
    
    def searchRecord(self):
        print("\n\n\t\t\t** Search Student Record **\n")
        roll = input("\t\t\tEnter roll number to search: ")
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        print("\n",71*'=')
                        print("\n\t\t\t   >> Student Record << \n")
                        print("\t\t\t Roll: ", row[0])
                        print("\t\t\t Full Name: ", row[1])
                        print("\t\t\t ID Number: ", row[2])
                        print("\t\t\t Program: ", row[3])
                        print("\t\t\t Year Level: ", row[4])
                        print("\n",71*'=')
                        break
            else:
                print("\n\n\t\t** Roll number not found in our database! **")
            
            self.exit()
    
    def updateRecord(self):
        print("\n\n\t\t\t** Update Student Information **\n")
        roll = input("\t\t\tEnter roll no. to update: ")
        index_student = None
        updated_data = []
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        index_student = counter
                        print("\n\t\t\tStudent found at index [",index_student, "] ")
                        print("\n",71*'=')
                        print("\n\t\t\t>> Fill-in New Record << \n")
                        student_data = []
                        for field in self.student_fields:
                            value = input("\t\t\tEnter " + field + ": ")
                            student_data.append(value)
                        updated_data.append(student_data)
                        print("\n",71*'=')
                        print("\n\n\t\t\t** Data saved successfully! **")
                        
                        print
                    else:
                        updated_data.append(row)
                    counter += 1
                    
        #checks if the student record is found or not
        if index_student is not None:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("\n\t\t** Roll number not found in our database! **\n")

        self.exit()

    def deleteRecord(self):
        print("\n\n\t\t\t ***Delete Student Information***\n")
        roll = input("\t\t\tEnter roll number to delete: ")
        student_found = False
        updated_data = []
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        student_found = True

        if student_found is True:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("\n",71*'=')
            print("\n\t\t\tRoll no. ", roll, "deleted successfully!")
            print("\n",71*'=')

        else:
            print("\n\t\t** Roll number not found in our database! **\n")

        self.exit()

    def admin_logout(self):
        pass
    
    def exit(self):
        input("\n\n\t\t\tPress enter key to continue...")
        print("\n")
