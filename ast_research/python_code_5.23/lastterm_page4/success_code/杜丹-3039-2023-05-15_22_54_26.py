ls=eval(input())
maxnum=max(ls)
minnum=min(ls)
ls2=ls.copy()
for num in ls2:
    if num==maxnum or num==minnum:
        ls.remove(num)
print(ls)



