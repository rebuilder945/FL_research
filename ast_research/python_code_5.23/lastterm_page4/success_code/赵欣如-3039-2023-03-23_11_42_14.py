ls1=eval(input())
ls2=ls1.copy()
a=max(ls1)
b=min(ls1)
for x in ls1:
    if x==a or x==b:
        ls2.remove(x)
print(ls2)
