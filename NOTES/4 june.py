# 4  :
"""
1.inheritance :
    a. singel  level inheritance 
    b. multiple  inheritance
    c. multi-level inheritanc
    d. hybrid
    e. hierarchy
2.polymorphism :
    a.method overloading
    b.method overriding
3.abstraction :
    a.abstract class
    b.class method , private method
4.encapsulation :
    a.get method
    b.set method    
""" 

# 1.inheritance : to inherit from another class
# a . single level  :   1 base class  1 derived class

"""class student:   # base class
    def display(self):
        print("student class")

class employee(student):   # employee derived class 
    def display(self):
        print("employee class")
    
e=employee()
e.display()
"""

"""class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class employee(student):
    def __init__(self, name, age,salary):
        # student.__init__(self,name,age)
        super().__init__(name,age)
        self.salary=salary
    def display(self):
        print("name :",self.name)
        print("age :",self.age)
        print("salary :",self.salary)
        
e=employee("hemali",20,25000)
e.display()
print(e.name)
print(e.age)
print(e.salary)
"""

class bank :
    def __init__(self,name,account_number,balance=0):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        print("deposited amount :",amount)
    
    def withdraw(self,amount):  # total  balance  = 30000 - 25000  > 10000
        if self.balance -amount >=10000:
            self.balance-=amount
            print("withdrawed amount :",amount)
        else :
            print("insufficient balance")
    
    def check_balance(self):
        print("balance :",self.balance) 

b=bank("hemali",7201000127890,25000)
b.deposit(5000)
b.withdraw(100000)
b.check_balance()