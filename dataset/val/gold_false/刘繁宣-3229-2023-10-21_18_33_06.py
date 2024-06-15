ls=eval(input())
ls2=ls[0:]
for i in range(len(ls)):
    if ls.count(i)>1:
        ls2.remove(i)
ls2.sort()
s=",".join(str(e) for e in ls2)
print(s)
