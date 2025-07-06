class Grandparent:
    def __init__(self, name):
        self.name = name

class Parent1(Grandparent):
    def __init__(self, name, age):
        Grandparent.__init__(self,name)
        self.age = age

class Parent2(Grandparent):
    def __init__(self, name, city):
        # super().__init__(name)
        Grandparent.__init__(self,name)
        self.city = city

class Child(Parent1, Parent2):
    def __init__(self,age,name, city, country):
        Parent1.__init__(self, name,age)
        Parent2.__init__(self, name,city)  
        self.country = country

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}, Country: {self.country}")

s1 = Child(20,"xyz","AHM", "India")
s1.display()
