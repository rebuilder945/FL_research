ls1=list(map(int,input().split(",")))
n,m=eval(input())
ls2=[]
if (n+1)<=len(ls1):
    for x in range(m):
        ls2.append(ls1[n])
        ls1=ls2
else:
    print("error")
