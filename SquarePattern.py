#python pattern program

import time
n = int(input("Enter the rows:"))

for i in range(n):
    for j in range(n):
        if(i==0 or j ==0 or i == n-1 or j == n-1 or i == j or (i+j) == n-1 or i in (4,5) or j in (4,5) ):
            #time.sleep(1)
            print("* ", end=" ")
        else:
            print(" ~" ,end=" ")
    print("\n")
