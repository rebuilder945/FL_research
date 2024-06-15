n=eval(input())
if n<0 or type(n) is float:
    print("illegal input")
else:
    for i in range(2,n+1):
        a=[]
        if i<=100:
            a.append(i)
        elif i>100:
            for x in range(len(str(i))//2):
                if str(i)[x]=str(i)[-x-1]:
                    a.append(i)
import math
for j in a:
    for p in range(2,int(math.sqrt(j))+1):
        if j%p==0:
            a.remove(j)
c=[2]+a
for q in c:
    print(q,end="")            

