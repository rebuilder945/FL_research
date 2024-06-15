ls=eval(input())
ls1=[]
k=0
for x in ls:
    if x==0:
        k=k+1
    else:
        ls1.append(x)
for x in range(k):
    ls1.append(0)
print(ls1)
