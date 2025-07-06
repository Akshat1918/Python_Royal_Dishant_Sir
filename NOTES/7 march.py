#pattern  : 

"""
*             * * * * *    1           5 4 3 2 1   1 2 3 4 5    1 2 3 4 5  
* *           * * * *      1 2         5 4 3 2     1 2 3 4      2 3 4 5  
* * *         * * *        1 2 3       5 4 3       1 2 3        3 4 5    
* * * *       * *          1 2 3 4     5 4         1 2          4 5 
* * * * *     *            1 2 3 4 5   5           1            5 
"""
"""
row  =5 
col =5

for(i=1; i<=5; i++)
    for(j=5; j>=i;j--)
        printf("*")
    printf("\n")
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

"""for  i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()
"""    

"""
* * * * *      1 2 3 4 5    5 4 3 2 1          *
  * * * *        1 2 3 4      5 4 3 2        * *   
    * * *          1 2 3        5 4 3      * * * 
      * *            1 2          5 4    * * * * 
        *              1            5  * * * * *

"""
for i in range(5,0,-1):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()