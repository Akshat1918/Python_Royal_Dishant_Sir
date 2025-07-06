#any digit  amg  : 3 digit  
"""
153 : 3 digit 
1**3   5**3  3**3  = 1 +125 + 27 = 153  

logic : 
r = num % 10   1  % 10 = 1 
sum = sum + (r*r*r)  = sum = 153  
num = num // 10   1 // 10 = 0

"""
# print(10/3)
# print(10//3)

"""
digit : 

1634 :  4 digit 
54748 : 5 digit
"""

# built in function  : len min max sorted sum 

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
 
# nested  loop  : 

#task : 1 ask user to enter the start and ending number print prime num bet two range. 

"""
start =int(input("enter the starting num : "))
end =int(input("enter the ending num : "))

for i in range(start,end+1):
    count =0
    for  j in range(1,i+1):
        if i % j ==0:
            count+=1
    if count ==2 : 
        print(i,end=" ")
"""
#task : 2 ask user to enter the start and ending number print perfect num bet two range. 
"""
start =int(input("enter the starting num : "))
end =int(input("enter the ending num : "))

for i in range(start,end+1):
    sum =0
    for  j in range(1,i):
        if i % j ==0:
            sum =sum +j
    if sum  ==i : 
        print(i,end=" ")
"""
#task : 3 ask user to enter the start and ending number print amg num bet two range. 
start =int(input("enter the starting num : "))
end =int(input("enter the ending num : "))

for i in range(start,end+1):
    sum =0
    digit=len(str(i))
    temp =i 
    for j in range(digit):
        r=temp % 10
        sum =sum + pow(r ,digit)
        temp = temp //10
    if sum ==i :
        print(i,end=" ")

# nest sess : pattern   , while  , while true  