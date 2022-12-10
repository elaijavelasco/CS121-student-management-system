import csv ,operator
import sys

class Manage_Student_Database:
    student_fields = ['ID No.', 'Full Name', 'Program', 'Block', 'Year Level']
    student_database = 'students.csv'

class Admin_Database:
    admin_fields = ['Username' , 'Password']
    admin_database = 'admin.csv'
 
class Admin(Admin_Database):
    def __init__(self):
        super().__init__(self)

    #function for admin login   
    def login(self):
        username = input("\n\t\t\tEnter username: ")
        if username not in Admin_Database.admin_database:
            print ("\n\t\t\tUsername invalid!")
            Admin.login(self)

        password = ""
        try:
            password = input("\t\t\tEnter password: ")
            if password == 'user':
                print("\n\t\t\tSuccessfully logged in!")
                Admin.adminMenu(self)
            else:
                print("\n\t\t\tUsername or password invalid!")
                Admin.login(self)    
        except ValueError:
            print("\n\t\t  Invalid Entry! You're unable to proceed.\n\n\n")
            sys.exit()
        
    def adminMenu(self):
        print("\n",71*'-')
        print("\n\t\t\t Manage Student Record")
        print("\n",71*'-')

        while True:
            print("\n\t\tMenu:\n")
            print("\t\t\t(1) Add New Student")
            print("\t\t\t(2) View Student Records")
            print("\t\t\t(3) Search Student Record")
            print("\t\t\t(4) Sort Student Record")
            print("\t\t\t(5) Update Student Record")
            print("\t\t\t(6) Delete Student Record")
            print("\t\t\t(7) Logout")

            self.choice = ""
            try:
                self.choice = int(input("\n\t\tWhat do you want to do? "))
            except ValueError:
                print ("\n\t\tInvalid Entry! Input should be a number.")
                Admin.backToMenu(self)

            if self.choice == 1:
                Admin.addRecord(self)

            elif self.choice == 2:
                print("\n\n\t\t\t ** Students Records **")
                Admin.viewRecords(self)
            
            elif self.choice == 3:
                print("\n\n\t\t\t** Search Student Record **\n")
                Admin.searchRecord(self)
                
            elif self.choice == 4:
                print("\n\n\t\t\t ** Sorted Records **")
                Admin.sortRecords(self)
            
            elif self.choice == 5:
                print("\n\n\t\t\t** Update Student Information **\n")
                Admin.updateRecord(self)
            
            elif self.choice == 6:
                print("\n\n\t\t\t *** Delete Student Information ***\n")
                Admin.deleteRecord(self)
            
            elif self.choice == 7:
                Admin.logout(self)
            
            else:
                print ("\n\t\tInvalid Entry! Choice should be from 1 to 6.")
                Admin.backToMenu(self)

    def addRecord(self):
        self.student_data = []

        print("\n",71*'=')
        print("\n\t\t\t >> Fill-in Information << \n")
        print("\t\tDon't leave it blank.")

        for field in Manage_Student_Database.student_fields:
            value = input("\t\t\tEnter " + field + ": ")
            if value == "":
                self.student_data.remove(value)
            self.student_data.append(value)
        print("\n",71*'=')

        with open(Manage_Student_Database.student_database, "a", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows([self.student_data])
            print("\n\n\t\t\t** Data saved successfully! **")
        Admin.backToMenu(self)
      
    def viewRecords(self):
        print("\n",71*'-')
        with open(Manage_Student_Database.student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in Manage_Student_Database.student_fields:
                print(x, end="\t|   ")
            print("\n",71*'-')

            for row in reader:
                for item in row:
                    print(item, end="\t|   ")
                print("\n")
            sys.exit()
    
    def searchRecord(self):
        idnumber = input("\n\t\t\tEnter ID number to search: ")
        with open(Manage_Student_Database.student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if idnumber == row[0]:
                        print("\n",71*'=')
                        print("\n\t\t\t   >> Student Record << \n")
                        print("\t\t\t ID Number: ", row[0])
                        print("\t\t\t Full Name: ", row[1])
                        print("\t\t\t Program: ", row[2])
                        print("\t\t\t Block: ", row[3])
                        print("\t\t\t Year Level: ", row[4])
                        print("\n",71*'=')
                        break
            else:
                Admin.notFound(self)
        sys.exit()
    
    def sortRecords(self):
        print("\n",71*'-')
        data = csv.reader(open('students.csv'), delimiter=',')
        data = sorted(data, key=operator.itemgetter(1))
        for x in Manage_Student_Database.student_fields:
            print(x, end="\t|   ")
        print("\n",71*'-')

        for row in data:
            for item in row:
                print(item, end="\t|   ")
            print("\n")
        sys.exit()
        
    def updateRecord(self):
        idnumber = input("\t\tEnter id number to update [e.g.: 2101442]: ")
        self.index_student = None
        self.updated_data = []

        with open(Manage_Student_Database.student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if idnumber == row[0]:
                        self.index_student = counter
                        print("\n\t\t\tStudent found at index [",self.index_student, "] ")
                        print("\n",71*'=')
                        print("\n\t\t\t>> Fill-in New Record << \n")
                        self.student_data = []
                        for field in Manage_Student_Database.student_fields:
                            value = input("\t\t\tEnter " + field + ": ")
                            if value == "":
                                self.student_data.remove(value)
                            else:
                                self.student_data.append(value)
                        self.updated_data.append(self.student_data)
                        print("\n",71*'=')
                        print("\n\n\t\t\t** Data saved successfully! **") 
                        Admin.backToMenu(self)
 
                    else:
                        self.updated_data.append(row)
                    counter += 1
                    
        #checks if the student record is found or not
        if self.index_student is not None:
            with open(Manage_Student_Database.student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(self.updated_data)
        else:
            Admin.notFound(self)

    def deleteRecord(self):
        idnumber = input("\t\t\tEnter ID number to delete: ")
        self.student_found = False
        self.updated_data = []
        with open(Manage_Student_Database.student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if idnumber != row[0]:
                        self.updated_data.append(row)
                        counter += 1
                    else:
                        self.student_found = True

        if self.student_found is True:
            with open(Manage_Student_Database.student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(self.updated_data)
            print("\n",71*'=')
            print("\n\t\t\tID Number ", idnumber, "deleted successfully!")
            print("\n",71*'=')
        else:
            Admin.notFound(self)
    
    def notFound(self):
        print("\n\t\t There's no such ID number in the database!\n")
        sys.exit()

    def backToMenu(self):
        response = int(input("\n\t\t\tType '0' to be back on Menu: "))
        if response == 0:
            Admin.adminMenu(self)
        else:
            print("\n\t\t  Invalid Entry! You're unable to proceed.\n\n\n")
            sys.exit()

    def logout(self):
        print("\n\n\n",73*'-')
        print("\n\t\t\tSuccessfully logged out!")
        print("\n",73*'-')
        sys.exit()