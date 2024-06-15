ls=list(int(input()))
a=max(ls)
b=min(ls)
ls1=ls.copy()
for x in ls:
    if x==a or x==b:
        ls1.remove(x)
print(ls1)        

