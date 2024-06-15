n=eval(input())
ls=[]
for i in range(len(str(n))):
    ls.append((int(str(n)[i])+5)%10)      #ls=[6,7]
import math
for i in range(math.ceil(len(ls)/2)):
    ls[i],ls[-(i+1)] = ls[-(i+1)],ls[i]     
m=str(ls[0])                              #ls=[6,7]
for i in range(len(ls)-1):
    m += str(ls[i+1])
print(m)                                  #67

