# inheri  ,  encap  , poli  :  hospital manag  system  

class person:
    def __init__(self,name,age):
        self._name=name  # protected 
        self._age=age
    def display(self):
        print(f"name : {self._name} , age : {self._age}")

class patient(person):   # single + encap  
    def __init__(self, name, age,disease):
        super().__init__(name, age)
        self.disease=disease
    
    def get_disease(self):  #encap 
        return self.disease

    def set_disease(self,new_disease):
        self.disease=new_disease
    
    def add_medical_history(self,medical_history):
        self.__medical_history=medical_history  # private 
    
    def show_medical_history(self):
        print(f"medical_history : {self.__medical_history}")
# multi level  : 
class inpatient(patient): 
    def __init__(self, name, age, disease,roomno):
        super().__init__(name, age, disease)
        self.room_no=roomno

    def display(self):
        print(f"name : {self._name} , age : {self._age} , disease : {self.disease} , room_no : {self.room_no}")

class doctor(person):
    def __init__(self, name, age,speciality):
        super().__init__(name, age)
        self.speciality=speciality
    
    def display(self):
        print(f"name : {self._name} , age : {self._age} , speciality : {self.speciality}")

class nurse:
    def __init__(self,name,age,shift):
        self.name=name
        self.age=age
        self.shift=shift
    
    def display(self):
        print(f"name : {self.name} , age : {self.age} , shift : {self.shift}")

class admin:
    def __init__(self,name,age,mor_shift):
        self.name=name
        self.age=age
        self.mor_shift=mor_shift
    def display(self):
        print(f"name : {self.name} , age : {self.age} , mor_shift : {self.mor_shift}")

class management(nurse,admin):
    def __init__(self,name,age,shift,mor_shift,salary):
        nurse.__init__(self,name,age,shift)
        admin.__init__(self,name,age,mor_shift)
        self.salary=salary
    def display(self):
        print(f"name : {self.name} , age : {self.age} , shift : {self.shift} , mor_shift : {self.mor_shift} , salary : {self.salary}")

class billing:
    def bill(self,patient,amount=0):
        print(f"patient : {patient} , amount : {amount}")


print("=========normal patient ==========\n")
p=patient("suresh",39,"diabetes")
p.add_medical_history("hypertension")

print("beofre  disease : ",p.get_disease())
p.set_disease("hypertension")
print("after disease : ",p.get_disease())
p.show_medical_history()

print("=========inpatient ==========\n")
it=inpatient("mahesh",67,"blood pressure",101)
it.add_medical_history("magaj no  prlm che")
it.display()

print("=========doctor ==========\n")
d=doctor("dr.jaival shah",30,"Nurologist")
d.display()

m=management("ramila",50,"night",0,12000)
m.display()

b=billing()
b.bill("mahesh",50000)

# 
"""
menu  driven  : 
1.add 
2.delete 
3.update 
4.search 
5.display

"""