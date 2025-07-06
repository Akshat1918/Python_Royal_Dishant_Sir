# list and string task  : 
"""
task : 1 

l1 = ["aba" , "1221" , "maam" , "12","abc" ]
output : ["aba" , "1221" , "maam"]
condition  : 
1.  len more than 2 
2. first  letter and  last letter are same . 

task : 2 
l1 = ["aba" , "1221" , "maam" , "12","abc" ]
output : ["aba" , "1221" , "maam" ]
seprate  pelindorme string in a list. 

task  : 3 
l1=["python" , "java" , "c++" , "c" ,"react"]
output =["python"]
print longest word in list. 
"""
# hint 2 : 
"""
l1 = ["aba" , "1221" , "maam" , "12","abc" ]
#      0        1         2       3     4 
l2=[]
for i in l1 : # aba 
    if i == i[: : -1]:  # aba ==
        l2.append(i)
print(l2)
"""

# hint : 3 
"""
l1=["python" , "java" , "c++" , "c" ,"react","languages"]
s1=""
for i in l1:
    if len(i)>len(s1):
        s1=i
print(s1)
"""

"""s1 ="python"
print(s1[: : -1])
"""
"""
task  : 4 
input  : [1,2,3,4,5,6,7,9,10]
output  :  second largest element is  : 9 
"""
# 1 4 9 7 2 3  : 1 2 3 4 7 9  


"""n=int(input("enter the num : "))
l1=[]
for i in range(1,n+1):
    num =int(input("enter the number  : "))
    l1.append(num)
print(l1)
sorted_list =sorted(l1)
print(sorted_list)
print(sorted_list[-2])
"""