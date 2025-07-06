# multi level inheritance  : 
"""
class - a 

class b  (a) 

class c (b)
"""

"""class a :
    def __init__(self):
        print("constructor  of a ")

class b(a):
    def __init__(self):
        super().__init__()   # calling the base  class constructor  == >a 
        print("constructor  of b ")

class c(b):
    def __init__(self):
        super().__init__()  # calling the base  class constructor  == >b
        print("constructor  of c ")


for i in range(3):
    print("objects \n")
    c1=c()

c1=c()
b1=b()
b1=b()
"""
# using constructor with arg  : 

"""class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name :",self.name)
        print("age :",self.age)

class student(person):
    def __init__(self,name,age,student_id):
        #person.__init__(self,name,age)
        super().__init__(name,age)
        self.student_id=student_id

class marks(student):
    def __init__(self,name,age,student_id,Marks):
        super().__init__(name,age,student_id)
        self.Marks=Marks
    def display(self):
        print("name :",self.name)
        print("age :",self.age)
        print("student id :",self.student_id)
        print("marks :",self.Marks)

students=[]
for i in range(3):
    print("\n.....enter the student detalis ....\n")
    name= input("enter name :")
    age=int(input("enter age :"))
    student_id=int(input("enter student id :"))
    # Marks=int(input("enter marks :"))
    marks2=[]
    for j  in range(3):
        m=int(input("enter the marks : "))
        marks2.append(m)  # 85  99 55
    student1 =marks(name,age,student_id,marks2)   # 
    students.append(student1)
for i in students:
    i.display()
"""

# multi-ple  inheritance  : 

"""
class a 

class b  

class c (a,b)
"""

"""class a :
    def __init__(self,name):
        self.name=name
        
class b : 
    def __init__(self,age):
        self.age=age
class c (a,b):
    def __init__(self,name,age,salary):
        a.__init__(self,name)
        b.__init__(self,age)
        self.salary=salary
    def display(self):
        print("name :",self.name)
        print("age :",self.age)
        print("salary :",self.salary)

c1=c("twisha",20,500)
c1.display()
"""        

class a :
    def __init__(self,name):
        self.name=name
        
class b : 
    def __init__(self,name):
        self.name =name
        
class c (a,b):
    def __init__(self,name,salary):
        a.__init__(self,name)
        b.__init__(self,name)
        self.salary=salary
    def display(self):
        print("name :",self.name)
        print("salary :",self.salary)

c=c("twisha",500)
c.display()
