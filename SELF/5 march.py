"""n=int(input("Enter the number : "))
sum=0
temp=n
for i in range(1,n+1):
    r=temp%10
    sum=sum+(r*r*r)
    temp=temp//10
if sum==n:
    print("armstrong number")
else:
    print("not an armstrong number")
"""
start=int(input("Enter the starting number : "))
end=int(input("Enter the ending number : "))
for i in range(start,end):
    sum=0
    for j in range(1,i):
        if i%j==0 : 
            sum = sum + j
    if(sum==i):
         print(i)