# private variable : 
"""
get , set access == > 

get  ==>  data  read, print  
set  ==> new value  
"""

"""class  student : 
    def __init__(self,name,salary):
        self.__name =name   # private variable
        self.__salary = salary  # private variable

    def get_name(self):
        return self.__name

    def set_salary(self,newsalary):
        self.__salary= newsalary      

    def get_salary(self):
        return self.__salary

s=student("yash",50000)
print("before using set method : ")
print(s.get_name())
print(s.get_salary())

s.set_salary(60000)
print("after using set method : ")
print(s.get_name())
print(s.get_salary())
"""

"""
class student :
{
    private: 
        string  name ; 
        int age ;
    
    public : 
        student(string  name , int age)
        {
            this->name =name; 
            this->age =age ; 
        }
        void display()
        {
            cout<<"name : "<<this->name<<endl;
            cout<<" age : "<<this->age<<endl;
        }
};

"""

# polimorphism : many forms of same function
"""
1. method overriding : 
2. method overloading:
"""
# over  riding : 
"""class student :
    def __init__(self):
        self.name="yash"
        self.age =20
        print("yash patel class is created.")
    
    def __init__(self):
        self.name ="rishi"
        print("rishi shah class is created.",self.name)

    def display(self):
        print("hello  yash ????")
    
    def display(self):
        print("hello  rishi ????")
    
s=student()
s.display()
"""

"""class  vehicle : 
    def speed(self):
        print("speed of vehicle")

class car(vehicle):
    def speed(self):
        print("speed of car")

class  bike(vehicle):
    def speed(self):
        print("speed of bike")

class truck(vehicle):
    def speed(self):
        print("speed of truck")

t=truck()
t.speed()
"""


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def calculation(self,length,breath=0):
        if breath==0:
            return length*length
        else :
            return length*length*breath

s=student("yash",20)
print(s.calculation(10))   #  length    10 *10 = 100 
print(s.calculation(10,20))  # 10 , 20 = 10 *20 = 200
