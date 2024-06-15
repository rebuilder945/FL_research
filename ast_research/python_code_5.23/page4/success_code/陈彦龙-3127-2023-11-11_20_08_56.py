n=eval(input())
ls1=[]
for x in range(1,n+1):
    ls1.append(x)
i=ls1[0]
ls1.pop(0)
ls1.insert(n,i)
print(ls1)
