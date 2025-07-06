# nested while : prime  perfect amg 

"""start=int(input("enter the start num : "))
end=int(input("enter the end num : "))

i=start
while i<=end:
    sum=0
    temp =i
    digit=len(str(i))

    while temp >0 :
        r= temp % 10 
        sum =sum +pow(r,digit)
        temp =temp //10 
    if sum ==i:
        print(i,end=" ")
    i+=1
"""

# pattern  : 
"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""

"""
i=1 
while i <=5:
    k=1
    while k<i:
        print(" ",end=" ")
        k+=1
    j=5
    while j>=i:
        print("*",end=" ")
        j-=1
    print()
    i+=1
"""

# while true  : 
"""
syntax : 

while True :
    print()
    i+=1
     break 
"""

# 1 - 10 : 

"""i=1 
while True:
    print(i)
    i+=1
    if i==11:
        break
"""

# user num : 
"""n =int(input("enter the num : "))
i=1
sum = 0
while True :
    sum =sum+i
    i+=1
    if i ==n+1:
        break
print("sum : ",sum)
"""

# cal : 
"""
1. add 
2. sub 
3. mul 
4. div 
5. mod 
6. add new num 
7 . exit
"""
"""
python  data type  : 

1.  string  : immutable  
2. list  :  mutable  
3. tuple  :  immutable  
4. dict : mutable  
5. set : mutable 
"""

# list :  mutable  :  you can changes in list 

"""l1 = [1,2,3,4,5,6,7,8,9,10,"ram"]
print(l1)
print(type(l1))
"""
# built in function  :  len  min  max sorted  sum  


"""l1= [100,1,2,3,4,90,6,3]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))
print(sum(l1))
"""

# method  : 

l1= [100,1,2,3,4,90,6,3]

# pos index start with  : 0  
# neg  index num start with  : -1

# l1.append("pratham")
# print(l1) 

# l1.clear()
# print(l1)

# l2= l1.copy()
# print(l2)

# print(l1.index(90))

# l1.insert(3,"yash")
# print(l1)

# l2=["kiwi", "apple"]
# l1.extend(l2)
# print(l1)

# l1.pop(2)
# print(l1)

# l1.remove(100)
# print(l1)

# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)


"""
task  : 1 
ask user to enter the number  and store in to list and print odd even sum in list . 
5 
l1= [1,2,3,4,5]
odd sum : 9
even sum = 6    
"""

l1=[]
for i in range(5):
    num=int(input("enter the number : "))
    l1.append(num)
print(l1)
oddsum = 0
evensum = 0
for i in l1 :
    if i  % 2 ==0:
        evensum += i
    else :
        oddsum += i
print(oddsum)
print(evensum)



# home work : 
"""
task : 2 
ask user to enter the number  and store in to list and seprate pelindrome list .
input  : [121,141,563,789,743,964,456]
output : [121,141]

task  : 3
ask user to enter the number  and store in to list and  seprate perfect element in to the list.

input  : [1,2,6,28,496,123]
output : [6,28,496]
"""