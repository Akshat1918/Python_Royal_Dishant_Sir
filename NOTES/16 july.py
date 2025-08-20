# class method  : 
"""
class method  :   cls 
modify the class itself
"""
"""class emp :
    com="KPMG"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print(self.name,self.age,self.salary)
    @classmethod
    def display_class(cls,nwe_name):

        print(cls.nwe_name)
        print(cls.com)
e=emp("john",23,1000)
e.display()
e.display_class()
emp.display_class("PWC")

"""

# static  method  : 
"""class cal :
    @staticmethod
    def sum(a,b):
        return  a+b

c=cal()
print(c.sum(12,13))
"""

# abstarction  : 
"""
1 . data hiding  
2 . security 

from  ABC  import  abc   == > abstarct base class ,@abstarctmethod 
class a(ABC):
    @abstarctmethod 
    def display(self):
        pass
abstarct base class ==>  no creation of object 
"""
from abc import ABC ,abstractmethod
"""class  vehicle(ABC):
    def engine_start(self):
        pass 
    def engine_stop(self):
        pass 
class car(vehicle):
    def engine_start(self):
        print("car engine start")
   
    def engine_stop(self):
        print("car engine stop")

class  bike(vehicle):
    def engine_start(self):
        print("bike engine start")
    
    def engine_stop(self):
        print("bike engine stop")

b=bike()
b.engine_start()
b.engine_stop()
c=car()
c.engine_start()
c.engine_stop()
"""

class  ATM(ABC):

    def __init__(self,name,age,balance):
        self.name=name
        self.age=age
        self.balance=balance
      
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def check_balnace(self):
        pass 

class SBI(ATM):
    def __init__(self, name, age, balance=0):
        super().__init__(name, age, balance)
    def authenticate(self,pin=1234,accno=79120001432):
        if pin==1234 and accno==79120001432:
            print("pin",pin,"accno",accno)
        else :
            print("not valid.")
   
    def  deposit(self,amt):
        self.balance+=amt
        print("amt deposit")
    
    def withdraw(self,amt):
        self.balance-=amt
        print("amt withdraw")
    
    def check_balnace(self):
        print("balance check",self.balance)
    
sbi=SBI("patel yash",20,50000)
sbi.authenticate()
sbi.deposit(1000)
sbi.withdraw(1000)
sbi.check_balnace()
sbi.authenticate(455,1234567)
sbi.deposit(1000)
sbi.check_balnace()