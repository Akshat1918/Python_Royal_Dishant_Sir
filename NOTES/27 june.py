# single level : 

class person : 
    def __init__(self,name,age):
        self.name = name
        self.age = age
class  customer(person):
    def __init__(self, name, age,accno):
        super().__init__(name, age)  # super() used to call  base  class constructor   
        # person.__init__(self, name, age) # person  ==>  constructor  call     
        self.accno =accno  

# multiple level   + multi - level  
class account (customer):
    def __init__(self, name, age, accno,balance):
        super().__init__(name, age, accno) 
        self.balance = balance 
    def  deposit(self,amount):
        self.balance +=amount 
        print("new  balance after depposit  : ",self.balance)
    def  withdraw(self,amount):
        self.balance -=amount
        print("new  balance after withdraw : ",self.balance)
# ple : 
class internetbanking:
    def login(self,user_id,password):
        print("login success with  user id  and  password: ",user_id,password)

class netbanking(account,internetbanking):
    def __init__(self,name, age, accno,balance,user_id,password,fees):
        super().__init__(name, age, accno,balance)
        self.fees =fees 
# hierarchy  :
class savingsacount(customer):
    def savings_feature(self):
        print("savings  feature")

class currentaccount(customer):
    def current_feature(self):
        print("current  feature")

# single level  : 

print("==============account holder================")
acc =account("hemali",21,7201245820,25000)
acc.deposit(5000)
acc.withdraw(2000)

# ple  + level : 
print("==================netbanking_account holder================")
net = netbanking("hemalini",22,7201245820,30000,12,"helu@12",500)
net.login("12","helu@12")
net.deposit(5000)
net.withdraw(2000)

# 
print("==================current account holder================")
cur=currentaccount("yash",20,7201245820)
cur.current_feature()
"""
task  : 1
you select  net banking  then: 
    1. create :  ==> user_id , password 
    2. login  :    ==> 1. id  2. password 

task  : 2 
    1. saving  acc : deposit  withdraw  + charges  ==> balance 20000 more  10 % charges
    2. saving  acc : deposit  withdraw  + charges  ==> balance 30000 more  20 % charges 
     
    """