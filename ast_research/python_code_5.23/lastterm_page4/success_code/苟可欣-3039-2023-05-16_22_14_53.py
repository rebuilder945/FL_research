ls=eval(input())
a=min(ls)
b=max(ls)
ls1=[]
for x in ls:
    if x==a or x==b:
        continue
    else:
        ls1.append(x)
print(ls1)
