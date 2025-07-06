# match  : 
"""
switch (choice )
{
    case 1 : 
        break ;
    case 2 : 
        break;
        default :
}
"""
"""a=int(input("enter the number  : "))
b=int(input("enter the number  : "))

print("welcome to calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modular")
print("6.exit")

choice =int(input("enter the choice : "))
match(choice):
    case 1:
        print("addition of two num : ",a+b)
    case 2 :
        print("subtraction of two num : ",a-b)
    case 3 :
        print("multiplication of two num : ",a*b)
    case 4:
        print("div of two num : ",a/b)
    case 5:
        print("mod of two num : ",a%b)
    case _:
        print("invalid choice")  
"""

# for loop  : 
"""
c syntax : 

for(start; end; inc/dec)

for variable name in range():
    print
"""

#  1 - 10 
"""for i in range(1,10):
    print(i,end=" ")
"""
# print(10/3)
# print(10//3) #floor div

# 10- 1 : 

# for i in range(10,0,-1):
#     print(i,end=" ")

# for i in range(1,10,3):
#     print(i,end=" ")


#user input  : 

"""
n=int(input("enter the number: "))

for i in range(0,n+1,2):
    print(i,end=" ")

"""    

# n natural num : 
"""
n=int(input("enter the number: "))
sum = 0
for i in range(1,n+1):
          
    sum =sum +i 
print("n natural num sum is  : ",sum)
"""
# print odd even sum using for loop : 

"""
n=int(input("enter the number: "))
evensum=0
oddsum=0

for i in range(1,n+1):
    if i % 2==0:
        evensum=evensum+i
    else :
        oddsum=oddsum+i
print("evensum : ",evensum)
print("oddsum : ",oddsum)
"""

# fact : 

"""n=int(input("enter the number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("fact is : ",fact)
"""

# prime num: 

n=int(input("enter the number  : "))
count =0
for i  in range(1,n+1):
    if n % i==0:
        count +=1
if count ==2:
    print(n,"is prime number")

# perfect  num  :   6  factors : 1,2,3,6   sum = 1+2+3 = 6  28  factors  : 1,2,4,7,14,28  sum = 1+2+4+7+14 = 28
# 100 factors : 1,2,4,5,10,20,25,50,100  sum = 1+2+4+5+10+20+25+50 = 117  not perfect 

# 