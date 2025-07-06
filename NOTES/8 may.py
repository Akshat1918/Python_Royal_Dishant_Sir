# local variable  : 

"""def x ():
    y = 100   # local variable  
    print(y)
x()
# print(y)   # local  variable can't access outside the function . 

"""
# global variable  : 

"""
x = 100 
def y ():
    print(x)
y()
print(x)  # global variable it is accessable  in both  outside the function  and in-side the function. 
"""


# global  variable  can be modify using global keyword . 

"""x = 100 
def y ():
    global x 
    x =200
    print(x)  # 200 
y()
print(x) # a.100  b.200 
"""
# lambda  function  : 
"""
one  liner function  :
syntax : 

lambda arg :  expression 
"""
# def sum(a,b):
#     return a+b 
# print(sum(10,20)) 

"""
a= lambda a,b : a+b 
print(a(10,20))
"""
"""
b =lambda x : x**2
print(b(3))
"""

# built in function  :  len min max sorted sum 

"""a= lambda x : sum(x)
print(a([1,2,3,4,50,6,7,8,9,10]))
"""

# if else  : 
# normal  : 

"""def  big():
    a=int(input("enter the number  : "))
    b=int(input("enter the number  : "))
    if  a>b :
        print("a is big")
    else :
        print("b is big")
big()
"""
# using lambda  : 
"""
x =lambda a,b : (a,"a is big") if a>b else (b,"b is big")
print(x(10,20))
"""

# filter  , map  : 
"""
l1=[1,2,3,4,5,6,7,8,9,10]
odd=[]
even=[]
for i  in l1 :
    if  i % 2==0:
        even.append(i)
    else :
        odd.append(i)
print(odd)
print(even)
"""
# filter  ==> infor filter   == > 12 mon  fin  trac . ==> june trac 
"""
l1=[1,2,3,4,5,6,7,8,9,10]
a=tuple(filter(lambda x : x % 2 ==0,l1)) 
b=list(filter(lambda x : x % 2 ==1,l1)) 

print(a)
print(b)
"""
# map : new list  
 
l1=[10,20,33,4,5] # *5 
l2=[2,3,4,5] # *5 

#  50  100 165 20  25
a=list(map(lambda x ,y: x*y,l1,l2)) 
print(a)

# task  : 1 
"""
l1= ["maam" , "1221" , "java" , "aba" , "python"]
output  = ["maam" , "1221","aba"]
"""