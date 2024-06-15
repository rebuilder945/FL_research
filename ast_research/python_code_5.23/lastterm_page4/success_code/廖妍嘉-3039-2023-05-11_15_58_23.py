ls=eval(input())
ls2=ls.copy()
a=max(ls)
b=min(ls)
for i in ls:
    if i==a or i==b:
        ls2.remove(i)
print(ls2)



