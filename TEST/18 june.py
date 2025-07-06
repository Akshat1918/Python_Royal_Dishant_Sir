# hierarchy  inheritance  : 

"""
class a :  #base class 

class b (a)  :  # deri 1

class c (a)  : # deri 2
"""

"""class a :   #base class 
    def display(self):
        print("class  a method")

class b (a):
    def display1(self):
        print("class  b method")

class c (a):
    def display2(self):
        print("class  c method")

objc=c()
objc.display2()
objc.display()
objc=b()
objc.display1()
"""


# with constructor : 

"""class  vehicle  : 
    def __init__(self,name):
        self.name =name 

class car (vehicle):
    def __init__(self, name,model):
        super().__init__(name)
        self.model= model

class bike(vehicle):
    def __init__(self, name,color):
        super().__init__(name)
        self.color= color
    def  display(self):
        print(self.name)
        print(self.color)
b =bike("R-one5","red")
# print(b.color)
# print(b.name)
b.display()
"""
# private variable  : 


class pratham:
    def __init__(self,age,clg):
        self.__age=age   # age  , clg  ==> private variable
        self.__clg=clg
    
    def display(self):
        print(self.__age)
        print(self.__clg)

    def __private_method(self):
        print("pratham love clg LJ")
    
    def display1(self):
        self.__private_method()
p=pratham(20,"LJ")
p.display()
p.display1()
# p.__private_method()  ==> not  access diectly  