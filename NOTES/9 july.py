# polymorphism  :  many  forms 
"""
==> 1 . method  over loding  :
==> 2 . method  over riding  :
"""

# method  over loading  : 

"""class calculation :
    def add(self,a=0,b=0,c=0):
        return a+b+c

c=calculation()
print(c.add(1))
print(c.add(2,6))
print(c.add(2,6,7))
"""

# method over riding  : 

"""class animal:
    def display(self):
        print("animal")

class cat(animal):
    def display(self):
        print("cat")

class dog(animal):
    def display(self):
        print("dog")

d=dog()
d.display()

c=cat()
c.display()  # cat
"""
"""
class yash :
    def __init__(self):
        print("yash")
    
    def __init__(self):
        print("saloni")
y=yash()
"""

# overloading + riding  : 

class shape :
    def area(self,a=0,b=0):
        return  a*b

class  circle(shape):
    def area(self, a=0, b=0):
        return 3.14*a*a

class  rectangle(shape):
    pass

r=rectangle()
print(r.area(2,8))

c=circle()
print(c.area(5))