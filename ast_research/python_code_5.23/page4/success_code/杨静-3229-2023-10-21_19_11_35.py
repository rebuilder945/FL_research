ls=eval(input())
ls2=[]
ls3=[]
ls4=[]
for x in ls:
    if x not in ls2:
        ls2.append(x)
for i in ls2:
    ls3.append(ls.count(i))
if min(ls3)>1:
    print('False')
else:
    for c in ls2:
        if ls.count(c)==1:
            ls4.append(c)
    print(ls4)
