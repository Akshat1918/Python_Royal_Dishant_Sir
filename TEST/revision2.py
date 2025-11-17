# print(10/4)
# print(10//4)

"""n= int(input("enter the num  : ")) # 1634 
sum = 0 
digit = len(str(n))  # 4 
temp =n  

for  i in range(digit):  # 4 
    r=temp % 10            # 1 % 10 = 1 
    sum =sum + pow(r ,digit)   # sum =1634
    temp = temp //10   # 1 //10 = 0 

if sum ==n:
    print("amg")
"""
"""for i in range(5,0,-1):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()"""

# ask user to enter the number and print first and last digit number sum. 

# n = int(input("enter the num : "))  
# last = n % 10
# first = n
# while first >=10:
#     first = first //10

# print("first : ",first)
# print("last : ",last)

# import math

# num = int(input("Enter a number: "))

# last = num % 10
# first = num // (10 ** int(math.log10(num)))

# print("Sum of first and last digits:", first + last)

# ask user to enter the number and print  middle  number sum. 

# n = int(input("enter the num : "))  # 1234
# length = len(str(n))  # 4
# sum = 0
# temp = n
# if length % 2 == 0:  # even
#     mid1 = length // 2  # 2
#     mid2 = mid1 + 1     # 3
#     for i in range(1, length + 1):  # 1 to 4
#         r = temp % 10
#         if i == mid1 or i == mid2:
#             sum = sum + r
#         temp = temp // 10
# else:  # odd
#     mid = (length // 2) + 1
#     for i in range(1, length + 1):
#         r = temp % 10
#         if i == mid:
#             sum = sum + r
#         temp = temp // 10
# print("sum : ", sum)

# s1= "today is wednesday and tomorrow is thursday." 

# print(len(s1))
# print(min(s1)) # ascii value
# print(max(s1))  # ascii value
# print(sorted(s1))


# s1= "Today Is Wednesday and tomorrow is thursday." 

# print(s1.capitalize()) # first letter in upper case
# print(s1.upper())
# print(s1.lower())
# print(s1.swapcase()) # lower to upper and upper to lower
# print(s1.title())   # first letter of each word in upper case
# print(s1.casefold()) # more stronger as it converts special char also to lower case


# s1= "Today Is Wednesday and tomorrow is thursday." 
# print(s1[0])
# print(s1[2 : 7])
# print(s1[-4])
# print(s1[2 : 10 : 2 ])
# print(s1[1 : 15 : 3 ])
# print(s1[ 4 : -6 : 2 ])
# print(s1[  :  : -1 ]) 

# s1= "today is  friday and tomorrow  is saturday."
# #    0123456
# # index : 
# # pos : l to  r : 0 
# # neg  : -1   r to l 

# print(s1.index("t"))
# print(s1.index("d"))
# print(s1.index("day"))
# print(s1.index("is"))
# print(s1.index("t",2,40))  # 2 start index  end  40 

# s1= "today is  friday and tomorrow  is saturday."
# print(s1.rindex("d"))    # r means reverse (reverse index)
# print(s1.rindex("is"))

# t1 = (1,2,3,4,5,6,7,8,9,10,"ram")
# print(t1)
# print(type(t1)) 

# t2 = 1,2,3,4,5,6,7,9,10,"twisha"
# print(t2)
# print(type(t2)) 

# t1 = (1,2,3,4,10,5,6,9,100)

# print(t1[2])
# print(t1[2 : 5])

# t1 = (1,2,3,4,10,5,6,9,100)
# print(t1.count(2))
# print(t1.index(10))

# t1 = ((10,20,30) , (40,50,60) , (70,80,90))
# l1 = []
# for i in t1:
#     l2 = list(i)
#     l2[-1] = 100
#     l1.append(tuple(l2))
# print(tuple(l1))

# d2={98 : 97, "yash" :97}
# print(d2)
# print(type(d2))

# d1={"phy" : 98,"maths" : 23}

# print(len(d1))
# print(min(d1))
# print(max(d1))
# print(sorted(d1))

# d2={"che" : 96,"s.s" :78}
# print(len(d2))
# print(min(d2))
# print(max(d2))
# print(sorted(d2))
# print(sorted(d2.values()))
# print(d2.keys())
# print(d2.values())
# print(d2.items())
# l1=["yash","pratham"]
# #{"yash" :89 , "pratham" :89}
# d2= dict.fromkeys(l1,89)
# print(d2)
# print(d2.get("s.s"))

# d1={"che" : 98,"phy" : 23,"s.s" :56}
# d1.pop("phy")
# print(d1)
# d1.popitem()
# print(d1)

# d1={}
# s =input("enter the string  : ")
# for i in s:
#     if i in d1:
#         d1[i]+=1
#     else: 
#         d1[i]=1
# print(d1) 

# s1 ={1,2,3,4,4,5,6,6,7,8,9,9,10}

# print(s1)
# print(type(s1))

# l1 = [1,2,3,3,4,4,5,5,6,6,7,8,8,9,10]
# s1 =set(l1)
# print(list(s1))

# s1 ={100,2,3,4,4,5,6,6,7,8,9,9,10}

# print(len(s1))
# print(min(s1))
# print(max(s1))
# print(sorted(s1))
# print(sum(s1))
# s1 ={100,2,3,4,4,5,6,6,7,8,9,9,10}

# s1.add(560)
# print(s1)
# s1.add(560)
# print(s1)

# s1.clear()
# print(s1)

# s1={1,2,3,4}
# s2={1,2,3}
# s3={1,2,3,4,5,6,7,8,9,10}


# print(s1.isdisjoint(s2))   # no common element in the set 
# print(s2.issubset(s1))

# print(s3.issuperset(s1))
# print(s3.issuperset(s2))


# s1={13,11,1,2,3,4,5,6,7,8,9,10}
# s1.discard(50)
# print(s1)

# # s1.remove(50)
# # print(s1)

# s1.pop()
# print(s1)

# s2={"yash"}
# s1.update(s2)
# print(s1)



# s1={1,2,3,4}
# s2={1,2,3}
# s3={1,2,3,4,5,6,7,8,9,10}

# # subset  superset   disjoint 

# print(s1.isdisjoint(s2))   # no common element in the set 
# print(s2.issubset(s1))

# print(s3.issuperset(s1))
# print(s3.issuperset(s2))

# s1={13,11,1,2,3,4,5,6,7,8,9,10}
# s1.discard(50)
# print(s1)

# s1.remove(50)
# print(s1)

# s1.pop()
# print(s1)

# s2={"yash"}
# s1.update(s2)
# print(s1)


# l1=[10,20,33,4,5] # *5 
# l2=[2,3,4,5] # *5 

# #  50  100 165 20  25
# a=list(map(lambda x ,y: x*y,l1,l2)) 
# print(a)


# class student :
#     def display(self):
#         print("hanshal patel")
#     def display(self):
#         print("live in ahm")
#     def display(self):
#         print("twisha live in pakistan.") 
# s=student()
# s.display()   



class pratham:
    def __init__(self,age,clg): 
        self.__age=age   # age  , clg  ==> private variable
        self.__clg=clg
    
    def display(self):
        print(self.__age)
        print(self.__clg)

    def __private_method(self):
        print("pratham love clg LJ")
    
    def display1(self):
        self.__private_method()
p=pratham(20,"LJ")
p.display()