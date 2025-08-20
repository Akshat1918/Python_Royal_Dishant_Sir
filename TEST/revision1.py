# task  : 1 
"""
Write a Python program to find the indexes of numbers in a given list below a given threshold.
Original list:
[0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
Threshold: 100
Check the indexes of numbers of the said list below the given threshold:
[0, 1, 2, 3, 7, 8, 9, 10]
"""

"""l1= [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
threshold = 100
indexes = [i for i, num in enumerate(l1) if num < threshold]
print(f"Original list: {l1}") 
print("Threshold:", threshold)
print("Indexes of numbers below the threshold:", indexes)"""

# task : 2 
"""
Write a Python program that accepts a list of integers and calculates the length and the fifth element.
Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
"""
"""l1 = [19, 19, 15, 5, 5, 5, 1, 2]
l=len(l1)
if l == 8 and l1[4] in l1 and l1.count(l1[4]) == 3:
    print(True)
else:
    print(False)
    """

# task : 1 
"""
input : dishant dipakkumar shah 
output : d.d.shah
"""
"""s1 = "dishant dipakkumar shah"
print(s1[0]+"."+s1[8]+"."+s1[19 : ])"""

"""task  : 2 

input  :  the lion  in the cage. 
outptu :  lion  in cage. 

task : 3 
replace the second  "r"  with hashtage. 
input :  restart 
output  :resta#t  

task  : 4 
replace first  and last  space with "_"
input  : today is  rcb and csk match .
output: today_is rcb and csk_match.
"""
"""l1= "the lion  in the cage."
s1 = l1.split()
s=s1[1]+ " "+s1[2]+" "+s1[4]
print(s)"""

"""l1="the lion  in the cage."
s1 = l1.split()
s1.remove("the")
s1.remove("the")
s=" ".join(s1)
print(s)
"""
"""s1="restart"
s2 = s1[0]
modify_string = s2+s1[1 :].replace("r","#")
print(modify_string)"""

#s1 = "today is  rcb and csk match ."


"""
d1 ={}

for i in range(3):
    name = input("enter the name  : ")
    marks =int(input("enter the marks "))
    d1[name]=marks
print(d1)   # {'sert': 56, 'wert': 15, 'qwert': 96}

sorted_marks =sorted(d1.values())
print(sorted_marks)  # [15 56 96 ]  []

d2={}
for i in sorted_marks:   # 
    for name , marks in d1.items():
        if marks == i:
            d2[name]=marks
print(d2)"""

d1={}
s =input("enter the string  : ")
for i in s:
    if i in d1:
        d1[i]+=1
    else: 
        d1[i]=1
print(d1)