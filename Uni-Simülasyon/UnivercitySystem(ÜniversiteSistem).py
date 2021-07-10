#-----------ALİCAN UZUNDEMİR-----------
#DB browser uzerınden verielri yukeleme yaptım,Bilgisayarınızda db browser kuru oluğundan emin olun
import sqlite3

class University:
    def __init__(self,name,country):
        self.name = name
        self.country = country
        self.status = True

        self.connectDataBase()

    def run(self):
        self.menu()
        

        choice = self.choice()

        if choice == 1:
            self.addStudent()
        if choice == 2:
            self.deleteStudent()
        if choice == 3:
            self.updateStudent()
        if choice == 4:
            while True:
                try:
                    orderby = int(input("1)Show All\n2)Faculty\n3)Department\n4)Type\n5)Status\n Select:  "))

                    if orderby < 1 or orderby > 5:
                        continue
                    break
                except ValueError:
                    print("Must be integer!")
            
            self.showAllStudent(orderby)
        if choice == 5:
            self.systemExit()
            print("Sistemden ciktiniz!!")


    def menu(self):
        print("***** {} Administration System *****".format(self.name))
        print("\n1)Add Student\n2)Delete Student\n3)Update Student\n4)Show All Students\n5)System exit\n")

    def choice(self):
        while True:
            try:
                process = int(input("Select: "))
                if process < 1 or process > 5:
                    print("Operation number must be between 1-5,please select correct number!!!")
                    continue

                break
            except ValueError:
                print("Operation is mus be integer number.Please write correct type!")
        
        return process    

    def addStudent(self):
        print("**** Student  Information **** ")

        name = input("Student's Name: ").lower().capitalize() #burada yazının büyük harfle baslamasını sagladık kücük arfte yasa yazı büyük harfle baslıcak.
        surname = input("Student's Surname: ").lower().capitalize()
        faculty = input("Student's Faculty: ").lower().capitalize()
        department = input("Student's Department: ").lower().capitalize()
        while True:

                try:
                    studentid = int(input("Student's ID: "))
                    break
                except ValueError:
                    print("Type must be integer(1-1000)")
            

        while True:
            try:
                typ = int(input("Student Education Type: "))
                if typ < 1 or typ >2:
                    print("Student's Education Type must be 1 or 2.\n") 
                    continue
                break
            except ValueError:
                print("Type must be integer(1 or 2)\n")

        status = "Active"
        
        self.cursor.execute("INSERT INTO Students VALUES('{}','{}','{}','{}','{}','{}','{}')".format(studentid,name,surname,faculty,department,typ,status))

        self.connect.commit()

        print("The student named {} {} succesfully added".format(name,surname))


    def deleteStudent(self):
        self.cursor.execute("SELECT * FROM students")

        allStudents = self.cursor.fetchall()

        convertAllStr = lambda x: [str(y) for y in x]

        for i,j in enumerate(allStudents,1):
            print("{}){} ".format(i," ".join(convertAllStr(j))))
        
        while True:
            try:
                select = int(input("Select the student to be deleted: "))
                break
            except ValueError:
                print("Please write correct type(int)")

        self.cursor.execute("DELETE FROM Students WHERE rowid={}".format(select))

        self.connect.commit()

        print("\nStudent succesfully deleted.")
                

                
    def updateStudent(self):
        self.cursor.execute("SELECT * FROM students")

        allStudents = self.cursor.fetchall()

        convertAllStr = lambda x: [str(y) for y in x]

        for i,j in enumerate(allStudents,1):
            print("{}){} ".format(i," ".join(convertAllStr(j))))
        
        while True:
            try:
                select = int(input("\nSelect the student to be update: "))
                break

            except ValueError:
                print("Please write correct type(int)")
        

        while True:
            try:
                updateSelect = int(input("1)Name\n2)Surname\n3)Faculty\n4)Department\n5)Studentid\n6)Education Type\n7)Status\n"))
                print("select: {}".format(updateSelect))
                if updateSelect < 1 or updateSelect > 7:
                    continue
                break

            except ValueError:
                print("It must be int!")

        operations = ["name","surname","faculty","department","studentid","typ","status"]
        

        if updateSelect == 6:
            while True:
                try:
                    newValue = int(input("Enter the new value: "))
                    if newValue not in (1,2):
                        continue
                    break
                except ValueError:
                    print("Please,it must be integer!\n")
            
            self.cursor.execute("UPDATE Students SET typ={} WHERE rowid={}".format(newValue,select))
        else:
            newValue = input("Enter the new value: ")
            self.cursor.execute("UPDATE Students SET {}='{}' WHERE rowid={}".format(operations[updateSelect-1],newValue,select))

        self.connect.commit()

        print("Update Success!")

            
            

        

    def showAllStudent(self,by):
        if by == 1:
            self.cursor.execute("SELECT * FROM students")

            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i,j in enumerate(allStudents,1):
                print("{}){} ".format(i," ".join(convertAllStr(j))))

        if by == 2:
            self.cursor.execute("SELECT faculty FROM Students")

            faculties = list(enumerate(list(set(self.cursor.fetchall())),1))

            for i,j in faculties:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
                    
            
            
            self.cursor.execute("SELECT * FROM Students WHERE faculty='{}'".format(faculties[select-1][1][0]))

            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i,j in enumerate(allStudents,1):
                print("{}){} ".format(i," ".join(convertAllStr(j))))

        if by == 3:
            self.cursor.execute("SELECT departmant FROM Students")

            departmants = list(enumerate(list(set(self.cursor.fetchall())),1))

            for i,j in departmants:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
                    
            
            
            self.cursor.execute("SELECT * FROM Students WHERE departmant='{}'".format(departmants[select-1][1][0]))

            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i,j in enumerate(allStudents,1):
                print("{}){} ".format(i," ".join(convertAllStr(j))))

        if by == 4:
            self.cursor.execute("SELECT typ FROM Students")

            typ = list(enumerate(list(set(self.cursor.fetchall())),1))

            for i,j in typ:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
                    
            
            
            self.cursor.execute("SELECT * FROM Students WHERE typ={}".format(typ[select-1][1][0]))

            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i,j in enumerate(allStudents,1):
                print("{}){} ".format(i," ".join(convertAllStr(j))))

        if by == 5:
            self.cursor.execute("SELECT status FROM Students")

            status = list(enumerate(list(set(self.cursor.fetchall())),1))

            for i,j in status:
                print("{}){}".format(i,j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("Must be integer!")
                    
            
            
            self.cursor.execute("SELECT * FROM Students WHERE typ={}".format(typ[select-1][1][0]))

            allStudents = self.cursor.fetchall()

            convertAllStr = lambda x: [str(y) for y in x]

            for i,j in enumerate(allStudents,1):
                print("{}){} ".format(i," ".join(convertAllStr(j))))
            
            
        
    def systemExit(self):
        self.status = False
        
    
    def connectDataBase(self):
        self.connect = sqlite3.connect("UNIVERCITY.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Students(name TEXT,surname TEXT,faculty TEXT,departmant TEXT,studentid Text,typ INT,status TEXT)")

        self.connect.commit()




UNIVERCITY = University("UNIVERCITY SUMULATION","Turkey")

while UNIVERCITY.status:
    UNIVERCITY.run()