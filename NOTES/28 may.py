#constructor  : use ==> direct object 
"""
1. default constructor  : 
2. non paramter const 
3. para meter const
4. const with default arg   
"""
# 1. default constructor  : 

"""class student :  # student ==> class  
    def __init__(self):   # def  ==> keyword  ==> __init__ ==> constrcutor  => self keyword
        print("yash patel.")

s=student()  # s object         
"""
# constructor over loading  : 
"""class  student :
    def __init__(self):
        print("my name is yash patel.")
    
    def __init__(self):
        print("best friend name is sujal.")

s=student()
"""
# function over loading  :
"""class student :
    def display(self):
        print("hanshal patel")
    def display(self):
        print("live in ahm")
    def display(self):
        print("twisha live in pakistan.") 
s=student()
s.display()   
"""

# 2. non parameter  const : 

"""
class student :  #student class 
    def __init__(self):  # __init__ => const 
        self.name ="hemali"
        self.area ="nikol"  # name  area clg ==> data member  
        self.clg="J.G" 
    
    def display(self):
        print("name : ",self.name)
        print("area : ",self.area)
        print("clg: ",self.clg)

s=student()
# s.display()
print(s.name)
print(s.clg)
print(s.area)
"""

# 3. para meter  : 

"""class student : 
    def __init__(self,name,age,salary):
        self.name =name 
        self.age =age 
        self.salary=salary
    
    def display(self):
        print("name :",self.name)
        print("age :",self.age)
        print("salary : ",self.salary)

s=student("yash",20,250000)
s.display()
"""

# 4. const with default arg  : 

class student :
    def __init__(self,name="deep",age=0):
        self.name =name 
        self.age=age 
    
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)

s=student("sujal",20)
s.display()

