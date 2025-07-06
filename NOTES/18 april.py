#set : mutable  ==>  chages in  set .  and no repeation allow in set.  

"""
s1 ={1,2,3,4,4,5,6,6,7,8,9,9,10}

print(s1)
print(type(s1))
"""
"""l1 = [1,2,3,3,4,4,5,5,6,6,7,8,8,9,10]
s1 =set(l1)
print(list(s1))"""

# built in function : len min max sorted  sum 

"""
s1 ={100,2,3,4,4,5,6,6,7,8,9,9,10}

print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
print(sum(s1))
"""

# method : 

# s1 ={100,2,3,4,4,5,6,6,7,8,9,9,10}

# s1.add(560)
# print(s1)
# s1.add(560)
# print(s1)

# s1.clear()
# print(s1)

# s2=s1.copy()
# print(s2)

# s1={1,2,3,4}
# s2={2,4,6,8}
# s3={1,2,3,4,5,6,7,8,9,10}

# union intersection  difference 

"""print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1 -s2 
print(s2.difference(s1))  # s1 -s2 
"""
# print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1)
# print(s1)

# print(s1.symmetric_difference(s2))

# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)

# s1={1,2,3,4}
# s2={1,2,3}
# s3={1,2,3,4,5,6,7,8,9,10}

# subset  superset   disjoint 

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

# frozen set : immutable  , repeation not allow  in fz. 

"""s1=frozenset({1,2,3,3,4,4,5})
print(s1)
print(type(s1))
"""
# s1={1,2,3,3,4,4,5}  # no slicing set 
# print(s1[3])

# ======================================function  ===========================================

"""
1. no  arg no return  
2. with arg no return 
3. no arg  with return  
4. with arg  with return  
"""

# 1. no arg  no return  

"""def sum():   # def keyword   sum  : ==> func name 
    a=10
    b=20           # func intialiation  
    c=a+b
    print(c)
sum()    # func calling  

"""

# 2. with arg no return  : 

"""def sum(a,b):
    c=a+b
    print(c)
a=int(input("enter the num : "))
b=int(input("enter the num : "))
sum(a, b)
"""

# 3. no arg  with return  

"""
def sum():
    a=int(input("enter the num : "))
    b=int(input("enter the num : "))
    c=a+b 
    return c 
print(sum())
"""

# 4. with arg with return  : 
"""def sum(a,b):
    c=a+b 
    return c
a=int(input("enter the num : "))
b=int(input("enter the num : "))

print(sum(a,b))
"""

# *arg  :  only numberic arg  

"""def sum1(*arg):
    sum =0
    for i in (arg):
        sum = sum + i
    print(sum)
sum1(10)
"""
# home work  : 
"""

"""