ls=eval(input())
ls2=[]
for i in ls:
    if ls.count(i)==1:
        ls2.append(i)
if len(ls2)==0:
    print(False)
else:
    ls2.sort()
    s=",".join(str(e) for e in ls2)
    print(s)
