"""for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*  ",end=" ")
    print("")
for i in range(4,0,-1):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*  ",end=" ")
    print("")"""


n=int(input("Enter a number: "))

n = abs(n)  # Ensure the number is positive
last_digit = n % 10  # Get the last digit

while n >= 10:
    n //= 10  
first_digit = n
    
result=first_digit+last_digit
print("Sum of first and last digit:", result)







