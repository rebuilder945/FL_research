lst=eval(input())
ls=[]
for x in lst:
    if lst.count(x)==1:
        ls.append(x)
if len(ls)==0:
    print('False')
else:
    ls.sort()
    ls=list(map(str,ls))
    print(",".join(ls))



