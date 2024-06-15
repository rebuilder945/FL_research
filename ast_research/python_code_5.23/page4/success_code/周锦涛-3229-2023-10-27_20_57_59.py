ls=eval(input())
ls1=[]
ls2=[]
for x in ls:
    if x not in ls1:
        ls1.append(x)
    else:
        ls2.append(x)
a=list(set(ls1)-set(ls2))
a.sort()
if a==[]:
    print('False')
else:
    b=','.join(str(i) for i in a)
    print(b)
