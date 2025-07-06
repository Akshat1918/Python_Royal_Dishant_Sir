"""def x ():
    y = 100   # local variable  
    print(y)
x()
#print(y)   # local  variable can't access outside the function ."""
"""
x=100
def y ():
    print(x)

y()
print(x)  # global variable it is accessable  in both  outside the function  and in-side the function.""" 

"""x=100
def y ():
    global x
    x=200
    print(x)  # 200
y()"""
""""
def sum(a,b):
    return a+b
print(sum(10,20))"""

"""a= lambda a,b : a+b 
print(a(10,20))
b =lambda x : x**2
print(b(3))"""

"""l1=[1,2,3,4,5,6,7,8,9,10]
a=tuple(filter(lambda x : x % 2 ==0,l1)) 
b=list(filter(lambda x : x % 2 ==1,l1)) 

print(a)
print(b)"""

"""l1=[10,20,33,4,5] # *5 
l2=[2,3,4,5] # *5 

#  50  100 165 20  25
a=tuple(map(lambda x ,y: x*y,l1,l2)) 
print(a)
"""
# task  : 1 
"""l1= ["maam" , "1221" , "java" , "aba" , "python"]
output  = ["maam" , "1221","aba"]
"""
"""l1= ["maam" , "1221" , "java" , "aba" , "python"]
l2=[]
for i in l1:
    if i == i[::-1]:
        l2.append(i)

print(l2)
"""
