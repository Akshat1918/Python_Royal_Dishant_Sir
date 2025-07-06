# while  : 
"""
syntax : 

i= intia 
while con : 
    print
    inc/dec  : i+=1 i-=1
"""

# 1-10 ; 
"""i=1
while i<=10:
    print(i,end=" ")
    i+=1
"""
# user num  : 
"""
n =int(input("enter the num : "))
i=1
while i<=n:
    print(i,end=" ")
    i+=2
"""
# prime  perfect amg : 
# amg  : 
"""n =int(input("enter the num : "))
digit = len(str(n))
sum = 0
temp = n

while temp > 0:
    r  = temp % 10
    sum = sum+pow(r,digit)
    temp = temp // 10
if n == sum:
    print("amg num")
"""
# task  : 1 
"""
ask user to enter the number and print first and last digit number sum. 
input : 1234 
output  sum : 1+4 = 5

task : 2
ask user to enter the number and print  middle  number sum. 
input : 1234 
output  sum : 2+3 = 5

"""

# nested while  : 
# prime  perfect amg : 

start =int(input("enter the num : "))  # 1
end =int(input("enter the num : "))  # 1000

i=start  # 1 

while i<=end:  # 1 < = 1000
    sum = 0
    j=1
    while j< i:
        if i % j ==0:
            sum =sum + j
        j+=1 
    if sum ==i:
        print(i,end=" ")
    i+=1

# next sess :  while pattern while true      