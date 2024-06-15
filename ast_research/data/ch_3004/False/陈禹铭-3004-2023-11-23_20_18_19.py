nums=eval(input())
ls=[]
for x in nums:
    for i in range(2,int(x**0.5)+1):
        if x%i!=0:
            ls.append(x)
        else:
            pass
ls2=[]
for x in ls:
    if x not in ls2:
        ls2.append(x)
print(ls2)
