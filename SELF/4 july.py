#file  handling  : 
"""
1 .read : exiting  only    ==>r 
2 .write: new file  , write  , exiting file  ==> over write  ==>w
3 .append: new file ,  write ,exiting  file  ==> append   ==>a

csv == > file  ==> comma separated values
open == > with open 
file .close()
file.seek() ==> cursor  position  move   

import  random as r 
"""
# write  mode : 
"""
with  open("yash.txt",'w') as  file:
    file.write("my name is yash patel.\n")
    file.write("live in ahm.\n")
    file.write("age is 20 yr old  only.\n")
    file.write("may be  GF .\n")
"""

"""
with  open("yash.txt",'w') as  file:
    file.write("no  GF i am single.\n")
    file.write("study in silver oak college.\n")
"""

# read  mode  : 

"""with  open("yash.txt","r") as  file:
    # context = file.read()  # all context are read at once 
    # context = file.readline()   # rerad only one  line at time 
    context = file.readlines()   # read  line by line given in list 

    print(context)
"""

# append mode : 
"""
with  open("hemali.txt",'a') as file:
    file.write("my name is hemali  thakkar.\n")
    file.write("age in 22.\n")
    file.write("live in village.\n")
    file.write("bcz of thakkar  huge  property.\n") 
"""

"""with  open("hemali.txt",'a') as file:
    file.write("bapunagar  village.\n")     
"""

"""
task  :  1 

ask user to enter the string  and  print vowel  and consonant  in seprate file . 

input : my name is yash patel.
vowel.txt = aeiaae
consonant.txt = my nms ysh ptl
"""


vowels = "aeiouAEIOU"
consonants = ""
for char in input("Enter a string: "):
    if char.isalpha():
        if char in vowels:
            with open("vowel.txt", 'a') as v_file:
                v_file.write(char)
        else:
            with open("consonant.txt", 'a') as c_file:
                c_file.write(char)
    elif char.isspace():
        continue
    else:
        print(f"Skipping non-alphabetic character: {char}")