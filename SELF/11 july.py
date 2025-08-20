class person:
    def __init__(self, name, age):
        self._name = name  # protected 
        self._age = age

    def display(self):
        print(f"name : {self._name} , age : {self._age}")


class patient(person):  # single + encapsulation  
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease
        self.__medical_history = ""

    def get_disease(self):  # encapsulation
        return self.disease

    def set_disease(self, new_disease):
        self.disease = new_disease

    def add_medical_history(self, medical_history):
        self.__medical_history = medical_history  # private

    def show_medical_history(self):
        print(f"medical_history : {self.__medical_history}")

    def display(self):
        print(f"name : {self._name} , age : {self._age} , disease : {self.disease}")


# multi-level inheritance 
class inpatient(patient):
    def __init__(self, name, age, disease, roomno):
        super().__init__(name, age, disease)
        self.room_no = roomno

    def display(self):
        print(f"name : {self._name} , age : {self._age} , disease : {self.disease} , room_no : {self.room_no}")


class doctor(person):
    def __init__(self, name, age, speciality):
        super().__init__(name, age)
        self.speciality = speciality

    def display(self):
        print(f"name : {self._name} , age : {self._age} , speciality : {self.speciality}")


class nurse:
    def __init__(self, name, age, shift):
        self.name = name
        self.age = age
        self.shift = shift

    def display(self):
        print(f"name : {self.name} , age : {self.age} , shift : {self.shift}")


class admin:
    def __init__(self, name, age, mor_shift):
        self.name = name
        self.age = age
        self.mor_shift = mor_shift

    def display(self):
        print(f"name : {self.name} , age : {self.age} , mor_shift : {self.mor_shift}")


class management(nurse, admin):
    def __init__(self, name, age, shift, mor_shift, salary):
        nurse.__init__(self, name, age, shift)
        admin.__init__(self, name, age, mor_shift)
        self.salary = salary

    def display(self):
        print(f"name : {self.name} , age : {self.age} , shift : {self.shift} , mor_shift : {self.mor_shift} , salary : {self.salary}")


class billing:
    def bill(self, patient, amount=0):
        print(f"patient : {patient} , amount : {amount}")


class menu:
    def __init__(self):
        self.patients = []

    def add(self):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        disease = input("Enter disease: ")
        p = patient(name, age, disease)
        history = input("Enter medical history: ")
        p.add_medical_history(history)
        self.patients.append(p)
        print("Patient added successfully.\n")

    def delete(self):
        name = input("Enter name of patient to delete: ")
        for i, p in enumerate(self.patients):
            if p._name == name:
                del self.patients[i]
                print("Patient deleted successfully.\n")
                return
        print("Patient not found.\n")

    def update(self):
        name = input("Enter patient name to update disease: ")
        for p in self.patients:
            if p._name == name:
                new_disease = input("Enter new disease: ")
                p.set_disease(new_disease)
                print("Disease updated successfully.\n")
                return
        print("Patient not found.\n")

    def search(self):
        name = input("Enter patient name to search: ")
        for p in self.patients:
            if p._name == name:
                p.display()
                p.show_medical_history()
                return
        print("Patient not found.\n")

    def display(self):
        if not self.patients:
            print("No patients in the system.\n")
        else:
            for p in self.patients:
                p.display()
                p.show_medical_history()


# ================== TESTING STATIC DATA ===================
print("========= Sample Data ==========\n")
p = patient("suresh", 39, "diabetes")
p.add_medical_history("hypertension")
print("before disease : ", p.get_disease())
p.set_disease("hypertension")
print("after disease : ", p.get_disease())
p.show_medical_history()

print("\n========= inpatient ==========\n")
it = inpatient("mahesh", 67, "blood pressure", 101)
it.add_medical_history("mental stress issue")
it.display()

print("\n========= doctor ==========\n")
d = doctor("dr.jaival shah", 30, "Neurologist")
d.display()

print("\n========= management ==========\n")
m = management("ramila", 50, "night", 0, 12000)
m.display()

print("\n========= billing ==========\n")
b = billing()
b.bill("mahesh", 50000)

# ================== MENU DRIVEN SYSTEM ===================
print("\n========= HOSPITAL MANAGEMENT MENU ==========\n")

m = menu()
while True:
    print("1. Add Patient")
    print("2. Delete Patient")
    print("3. Update Patient Disease")
    print("4. Search Patient")
    print("5. Display All Patients")
    print("6. Exit")

    ch = input("Enter your choice (1-6): ")
    print()
    if ch == '1':
        m.add()
    elif ch == '2':
        m.delete()
    elif ch == '3':
        m.update()
    elif ch == '4':
        m.search()
    elif ch == '5':
        m.display()
    elif ch == '6':
        print("Exiting system. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")
