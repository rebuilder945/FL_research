lst=eval(input())
ls=lst.copy()
for x in lst:
    if ls.count(x)!=1:
        ls.remove(x)
print(ls)
