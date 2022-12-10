# Student Management System
A console application coded in Python programming language that used ```csv``` as database for storing records. The main focus of this console app is to allow the users to manipulate student information stored in the database.  This project is a user-friendly application created to store and monitor student records conveniently. 

## Overview


## Features
Student Management System provides the following features:
#### Main App Menu UI
#### Admin Mode                                                           
+ Admin Login                                                              
+ Admin Menu                                                                 
  * Add student records that will be stored in database                      
  * View the stored student records
  * Search student records 
  * Sort student records in the database
  * Update the stored records
  * Delete specific student record
#### Student Mode
+ Student Menu
  * View and retrieve records from database
  * Sort records for easy viewing
  * Search certain student record

## Dependencies
+ All codes are written in ```Python 3```.
+ Some codes depends on the ```csv``` module.
  * ```Admin.py```
  * ```Student.py```
+ Some codes depends on the ```sys``` library

## Description of Files
Non-Python files:

filename                |  description
------------------------|------------------------------------------------------------------------------------
README.md               |  Text file (markdown format) description of the project.
students.csv            |  CSV file, used as database for student records.
admin.csv               |  CSV file, used as database for admin login information.

Modules:

filename                |  description
------------------------|------------------------------------------------------------------------------------
App.py                  |  Contains the main app menu functions
Admin.py                |  Contains the functions that only the Admin user can perform
Student.py              |  Contains the functions that the Student can only perform to use the program

Python files:

filename                |  description
------------------------|------------------------------------------------------------------------------------
Main.py                 |  Python file that contains the driver code 

 
## 💻 Installation
1. Click [Student Management System](https://github.com/elaijavelasco/CS121-student-management-system.git) to be directed to the project's repository.
2. Click on the Code button, then download the repository as ZIP file.
3. Locate the downloaded ZIP file, likely in your Downloads folder, and unzip it.
4. Open the unzipped or the extracted folder and find ```Main.py``` file.
5. Open the file via any IDE that supports Python programming language.
6. Then, run the file to launch the application.

## 🔗 Project Demo

## 🤝 Acknowledgements
+ [GeeksForGeeks](https://www.geeksforgeeks.org/) were incredibly helpful while I was building the program
+ [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet?fbclid=IwAR2wjT8IG-2nDMH-PZWVG3MtUFPcu9asQ-bJfOUmn3T2H8QrLRYxVSDuqZ8) for quick reference 
+ [Python](https://www.python.org/) for reference in using [csv](https://docs.python.org/3/library/csv.html)
