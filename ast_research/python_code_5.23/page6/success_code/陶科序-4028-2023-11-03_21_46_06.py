n = eval(input())
c= ""
import copy
if n == int(n)and n >0:
    for i in range(2,n):
        for j in range(2,i-1):
            if i%j == 0:
                break
        else:
            i = int(i)
            i = str(i)
            if i == i[::-1]:
                print(i,end=" ")
else :
    print("illegal input")
