class Person:
    def __init__(self,first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name

    def get_email(self):
        print(f"{self.first_name}.{self.last_name}.school@edu.ge")

    def my_name(self):
        print(f"hi my name is  {self.first_name}, and my last name is {self.last_name} this is my email adress {self.get_email}")



class Lecturer(Person):

    def __init__(self,first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_email(self):
        print(f"{self.first_name}.{self.last_name}@edu.ge")

    def my_name(self):
        print(f"hi i am lecturer and my name is  {self.first_name},  my last name is {self.last_name} here is  my email adress  {self.get_email}"
              f" and i get this much monthly {self.salary} ")

class Student(Person):

    def __init__(self,first_name, last_name,  courses=[]):
        super(). __init__(first_name, last_name)
        self.courses = courses


    def get_email(self):
        print(f"{self.first_name}.{self.last_name}.1@edu.ge")

    def my_name(self):
        print(f"hi i am student, my name is {self.first_name}, my last name is {self.last_name}, this is my email adress {self.get_email},"
              f"and these are my courses {self.courses}")

p1 = Person("Ana-Maria", "Phiphia")
p1.my_name()
p1.get_email()
L1 = Lecturer( "Nini", "kvinikadze", 1000)
L1.get_email()
L1.my_name()
S1 = Student("anamaria", "phiphia", " pizika, matematika, biologia")
S1.my_name()
S1.get_email()

#davaleba2
class Libraryitem:

    def __init__(self,title,subject,status = "available" or "occupied"):
        self.title = title
        self.subject = subject
        self.status = status

    def booking(self):
        if self.status == "available":
                print("gatana shesadzlebelia")
        elif self.status == "uccupied":
                print("ar hsegidzliat gatana")

class Book(Libraryitem):

    def __init__(self,title,subject,status,isbn,authors):
        super().__init__(title,subject,status)
        self.isbn = isbn
        self.authors = authors


class Magazine(Book):
    def __init__(self,title,subject,status, journalname,volume):
        super().__init__(title,subject,status)
        self.journalname = journalname
        self.volume = volume


        
class CD(Magazine):
    def __init__(self,title,subject,status):
        super().__init__(title,subject,status)


b1 = Book("sapiens","history","available",6,"noah, harari")
b1.booking()
b2 = Magazine("todays news","daily news","available", "newss", 20)
del b2.title
del b2.subject
b2.booking()
c1 = CD("title","subject","occupied")
del c1.subject
c1.booking()


#3

class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def str(self):
        print(f"hi, i am {self.firstname} ")
class Employee(Person):

    def __init__(self,firstname,lastname,age,profession,monthly_salary,working_hours):
        super().__init__(firstname,lastname,age)
        self.profession = profession
        self.monthly_salary = monthly_salary
        self.working_hours = working_hours

    def hourly_salary(self):
        print(100)
class Doctor(Employee):
    def __init__(self,firstname,lastname,age,profession,monthly_salary,working_hours):
        super().__init__(firstname,lastname,age,profession,monthly_salary,working_hours)
    def str(self):
        print(f"hi i am {self.firstname}")
    def hourly_salary(self):
        print(100)
    def perform_operation(self):
        print("that's it ")

p1 = Person("natali","shelia",17)
p1.str()
e1 = Employee("natali","shelia",17,"life coach",30000,10)
e1.hourly_salary()
d1 = Doctor("natali","shelia",17,"life coach",30000,10)
d1.perform_operation()






















