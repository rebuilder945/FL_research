import math
n = eval(input())
b=0
if n >100:
    for i in range(100,n+1):
        a=int((math.log10(i))//1)
        c=0
        for x in range(0,a+1):
            c+=int(str(i)[x])**3
        
        if c == i:
            print(i)
            b=1
if b != 1:
    print("none")

            

