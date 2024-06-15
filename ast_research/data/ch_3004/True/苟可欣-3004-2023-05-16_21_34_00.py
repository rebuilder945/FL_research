ls=eval(input())
ls1=[]
for x in ls:
    if x==1 or x==0:
        continue
    else:
        k=0
        for n in range(2,x//2+1):
            if x%n==0:
                k=k+1
        if k==0:
            ls1.append(x)
print(ls1)
