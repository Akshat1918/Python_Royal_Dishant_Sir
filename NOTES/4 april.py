# tuple : immutable   ==> you can't changes in tuple  
"""
t1 = (1,2,3,4,5,6,7,8,9,10,"ram")
print(t1)
print(type(t1)) 

t2 = 1,2,3,4,5,6,7,9,10,"twisha"
print(t2)
print(type(t2)) 
"""
# built in function  :  len  min max sorted sum 

"""
t1 = (1,2,3,4,10,5,6,9,100)
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sum(t1))
"""
# slicing  : 
"""
t1 = (1,2,3,4,10,5,6,9,100)

print(t1[2])
print(t1[2 : 5])
"""
# method : 
"""t1 = (1,2,3,4,10,5,6,9,100)
print(t1.count(2))
print(t1.index(10))
"""

# task  : 1 
"""
t1 = (1,2,3,4,10,5,6,9)
output : (1,2,3,4,10,5,6,9,"yash")
"""

"""t1 = (1,2,3,4,10,5,6,9)
l1=list(t1)
l1.append("yash")
print(tuple(l1))
"""

# task  : 2 
"""
input  t1:((10,20,30) , (40,50,60) , (70,80,90))
output  : ((10,20,100) , (40,50,100), (70,80,100))
"""

"""t1 = ((10,20,30) , (40,50,60) , (70,80,90))
l1 = []
for i in t1:
    l2 = list(i)
    l2[-1] = 100
    l1.append(tuple(l2))
print(tuple(l1))
"""