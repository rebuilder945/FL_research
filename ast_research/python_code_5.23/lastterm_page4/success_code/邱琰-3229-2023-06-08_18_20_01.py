n=eval(input())
ls=[]
for i in n:
    if i not in ls:
        ls.append(i)
if len(ls)!=0:
    ls.sort()
    ls2=[str(x) for x in ls]
    print(','.join(ls2))
else:
    print('False')
