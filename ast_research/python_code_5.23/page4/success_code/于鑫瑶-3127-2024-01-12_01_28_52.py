n=eval(input())
ls1=[x for x in range(n+1)]
ls2=[]
for x in ls1:
    if x>=2:
        ls2.append(x)
ls2.append(1)
print(ls2)

