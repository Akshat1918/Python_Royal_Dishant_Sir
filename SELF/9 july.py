#polymorphism example using same class mixing method overloading and method overriding

"""class Animal:
    def sound(self):
        return "Some generic animal sound"
    def info(self):
        return "This is an animal"
class Dog(Animal):
    def sound(self):
        return "Bark"
    
    def info(self):
        return "This is a dog"
class Cat(Animal):
    def sound(self):
        return "Meow"
    
    def info(self):
        return "This is a cat"

    def animal_sound(animal):
        print(animal.sound())
        print(animal.info())

c=Cat()
d=Dog()
print(c.info())
"""

class shape:
    def area(self):
        return "Area of shape"
    
    def perimeter(self):
        return "Perimeter of shape"