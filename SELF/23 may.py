class student:

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = student()
s1.display()