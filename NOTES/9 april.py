# dict  : mutable ==>change  it.==> key value  

"""
d1={"phy" :98,"maths" :23}

# phy ==> key   value  98 
# maths ==> key value  : 23 
print(d1)
print(type(d1))
"""
"""d2={98 : 97, "yash" :97}
print(d2)
print(type(d2))
"""
# buit in function  : len min  max sorted 

#d1={"phy" : 98,"maths" : 23}
"""""
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""

"""d1["che"] =89
print(d1)
print(sorted(d1)) # sorted by key
print(sorted(d1.values())) # sorted by value
"""
# method  : 

"""d1={"che" : 98,"phy" : 23}

#d1.clear()
print(d1)
d2 = d1.copy()
print(d2)
print(d1.keys())
print(d1.values())
print(d1.items())
"""

"""l1=["yash","pratham"]
#{"yash" :89 , "pratham" :89}
d2= dict.fromkeys(l1,89)
print(d2)
print(d1.get("s.s"))
d1.update(d2)
print(d1)
d1={"che" : 98,"phy" : 23,"s.s" :56}
"""
# d1["che"] =23
# print(d1)

d1={"che" : 98,"phy" : 23,"s.s" :56}
"""d1.pop("phy")
print(d1)
d1.popitem()
print(d1)
"""
"""d1.setdefault("chem",26)
print(d1)  
#If the key exists in the dictionary, it returns the existing value.
#If the key does not exist, it adds the key with the specified default value and returns that default."""
"""d1={"che" : 98,"phy" : 23,"s.s" :56}

print(d1[0])   no slicing in dict 

"""
# task  : 1 
"""
ask user to enter the 5  student name and marks  store in the dict. 

input  : yash  56 pratham  23   jaival  89  utsav 99  twisha  55 
output : {"yash" : 56 , "pratham" : 23 , "jaival" :89 , "utsav" :99,"twisha :55"}
"""

"""d1 ={}

for i in range(3):
    name = input("enter the name  : ")
    marks =int(input("enter the marks "))
    d1[name]=marks
print(d1)   # {'sert': 56, 'wert': 15, 'qwert': 96}
"""

"""
sorted_marks =sorted(d1.values())
print(sorted_marks)  # [15 56 96 ]  []

d2={}
for i in sorted_marks:   # 
    for name , marks in d1.items():
        if marks == i:
            d2[name]=marks
print(d2)
"""
#task  : 2 
"""
ask user to enter the string  and count the letter  and store in to the dict 
input  : mississppi 
output : {'m' :1 ,'s':4, 'i' :3 ,'p' :2}
"""
"""d1={}
s =input("enter the string  : ")
for i in s:
    if i in d1:
        d1[i]+=1
    else: 
        d1[i]=1
print(d1)  
"""
# task : 3 
"""
count the occurance of word in the dict  : 
input  : ["apple" , "banana", "apple" , "kiwi" , "banana" , "apple"]
output :{"apple" :3 ,"banana" :2 ,"kiwi" :1}
"""
"""l1 = ["apple" , "banana", "apple" , "kiwi" , "banana" , "apple"]
d1={}
for i in l1:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1) """

# task : 4 
"""
swap the key value in dict : 

input  : {"yash" : 98 , "dev" : 78 , "hansal" : 99}
output  : {98 : "yash" , 78 :"dev" , 99 : "hansal"}
"""
