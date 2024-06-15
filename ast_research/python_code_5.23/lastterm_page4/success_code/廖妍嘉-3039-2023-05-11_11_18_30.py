ls=eval(input())
a=max(ls)
b=min(ls)
ls2=ls.copy()
for i in ls:
    if i==a or i==b:
        ls2.remove(i)
print(ls2)
