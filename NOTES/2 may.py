# emp  manag  system  : 
"""
1. add  / create   :  dict  ,  list  
2. update  
3. delete  
4. display  
5. search  
"""
emp={}
def addemp():
    id=int(input("enter the id : "))
    name=input("enter the name  : ")
    age= int(input("enter the age  : "))
    salary= int(input("enter the salary  : "))
    emp[id]={"name" :name,"age":age,"salary" :salary,}
    print("employess added successfully")

def update():
    id=int(input("enter the id : "))
    if id in emp:
        name=input("enter the name  : ")
        age= int(input("enter the age  : "))
        salary= int(input("enter the salary  : "))
        emp[id]={"name" :name,"age":age,"salary" :salary,}
    else :
        print("id is not  found")
    print("employees data update successfully.")

def delete ():
    id=int(input("enter the id : "))
    if id in emp:
        del emp[id]
    else :
        print("id is not  found")
    print("employees data delete successfully.")

def display():
    for  id , detalis in emp.items():   # key value 
        print(f"id :{id}, name :{detalis['name']},age :{detalis['age']},salary :{detalis['salary']}")
    print("all employess display sucessfully.")

def main():
    print("welcome to employees manag system")
    while True:
        print("1.add")
        print("2.update")
        print("3.delete")
        print("4.display")
        print("5.exit")
        choice =int(input("enter the choice :"))

        if choice==1:
            addemp()
        elif choice==2:
            update()
        elif choice ==3:
            delete()
        elif choice ==4:
            display()
        elif choice==5:
            print("thank you")
            break
        else:
            print("invalid choice")

main()


"""
display() : 
emp ={
    id   name        age salary
    1     yash patel 20  74000 
    2  jaival shah   20  95000 
}
delete  : 
id   name        age salary
    1     yash patel 20  74000 
    2  jaival shah   20  95000 
    
"""