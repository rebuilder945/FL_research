ls= eval(input())
a= max(ls)
b= min(ls)
ls2=ls.copy()
for x in ls:
    if x==a or x==b:
        ls2.remove(x)
print(ls2)
