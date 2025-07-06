# list  : 
"""
input  : l1 = [[1,2] , [3,4] , [5,6]]
output  : l1 =[1,2,3,4,5,6]
"""
"""
hint : 
c  :     
3*3 :    
1 2 3      1 2 
4 5 6      3 4 
7 8 9      5 6 

for (i=0; i<3; i++)
    for(j=0; j<3; j++)
"""

"""l1 =[[1,2] , [3,4] , [5,6]]
l2=[]

for i in l1 :
    for j in i:
        l2.append(j)
print(l2) 
"""
# while true  : 

"""i=1 
while True:
    print(i)
    i+=1
    if i==10 : 
        break 
"""

# tuple  :immutable 

"""
t1 = (1,2,3,4,5,65)
print(t1)
print(type(t1))

"""
"""
t1 = (1,2,3,4,5,65)

print(t1[0]) 
"""

# convert  : 
"""t1 = (1,2,3,4,5,65)
# output  : (1,2,3,4,5,65,"jaival")
l1= list(t1)
l1.append("jaival")
print(tuple(l1))
"""

# task : 1 

# t1 = ([],)
# t1[0].append(1)
# t1[1].append(3)
# t1[2].append(4)
# t1[3].append(5)

# print(t1)

"""
a. ([1,3,4,5])  d d  
b. indexerror  j d  s s u  j p k 
c. (1,3,4,5,[])  s h 
d .none      j a c y  d 
"""
# l1 =[()]
# l1.insert(5,5)
# print(l1[0])

# a. [()]  s 
# b. error      u s p y   j  
# c .()  y c c h  k p  j  d 
# d. none  d 

"""l1 =[1,2,3,4,5,6,7]
l1.insert(3,"patel")
print(l1)
"""

l1 =[(5,30),10,20]
#    0  1 2
# [(5,2)]   ==> 0  (0,1)  
# 10   ==> 1 
# 20   ==> 2 
# print(l1[0])

# print(l1[0])

# print(l1.index(30))


t1 =(1,30,[30])

print(t1.index(30))