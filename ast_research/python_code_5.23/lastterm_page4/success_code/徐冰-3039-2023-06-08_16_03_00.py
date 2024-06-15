ls=eval(input())
ls1=[]
a=max(ls)
b=min(ls)
for i in ls:
    if i!=a and i!=b:
        ls1.append(i)
print(ls1)
