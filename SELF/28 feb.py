"""sum=0
for i in range(1,11):
    sum = sum + i
print("The sum of first 10 natural number is ",sum)"""

"""for i in range(1,10,3):
    print(i,end=" ")"""
#for i in range(10,0,-1): 
 #   print(i,end=" ")
n=int(input("enter the number  : "))
count =0
for i  in range(1,n+1):
    if n % i==0:
        count +=1
if count ==2:
    print(n,"is prime number")
else:
    print(n,"is not a prime number")