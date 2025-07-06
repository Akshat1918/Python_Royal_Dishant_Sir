# slicing  : 

#l1 = [10,20,30,40,500,60,70,80,90,1000]
# index : 0 pos  : l  to  r  
# neg  : -1      : r to l 

"""print(l1[0])
print(l1[-2])
print(l1[2 : 5])   # 2 start index   5 end index
print(l1[ : 6])
print(l1[ 1: ])
print(l1[ : ])
print(l1[ : -2])
print(l1[ 2: 8 : 2])  # 2 start   8 stop   2 step 
print(l1[ 1: 8 : 3])  # 1start   8 stop   3 step 
print(l1[ :  :  -1])

"""

# print(l1.count(1000))

"""
task : 1 

ask user to enter the number and store in to the list and remove duplicate element in list . 

l1 = [12,3,3,4,6,7,8,9,9,10]
output  : [12,3,4,6,7,8,9,10]

task  : 2 

ask user to enter the number and store in to the list and check the condition .

condition 1. 19 element at least  3  time  and 5  element come at least 2  time  

l1= [1,2,19,19,19,5,5,3]
output  : true  

l1= [1,2,19,19,5,3]
output  : False   

"""

"""
===>    Task 1
l1 = [12,3,3,4,6,7,8,9,9,10]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)  # 12 3 
print(l2)
"""

"""
===>    Task 2
l1 = [1,2,19,19,19,5,5,3]
d1 = {}
for i in l1:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
print(l1)
print(d1)
count_19 = d1.get(19, 0)
count_5 = d1.get(5, 0)
if count_19 >= 3 and count_5 >= 2:
    print("True")
else:
    print("False")
"""