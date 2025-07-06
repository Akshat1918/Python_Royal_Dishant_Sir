"""l1=[2,3,4,6,1,5,10]

l1.sort()
print(l1)
l1.append("ram")
print(l1)
l1.reverse()
print(l1)
l1.reverse()
print(l1)
"""
"""l1=[2,3,4,5,6]
l2=[]
for i in range (1,6):
    for j in range(1,6):    
        l2[i]=l1[i]*2

print(l2)
"""
"""Write a Python program to check a given list of integers where the sum of the first i integers is i.
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True"""

lst = [0, 1, 2, 3, 4, 5]

valid = True
for i in range(len(lst)):
    if sum(lst[:i+1]) != i:
        valid = False
        break

print(valid)

