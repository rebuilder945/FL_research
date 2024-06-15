ls1=eval(input())
ls2=[]
for x in ls1:
    if ls1.count(x)==1:
        ls2.append(x)
    else:
        continue
if ls2==[]:
    print('False')
else:
    ls2.sort()
    ls3=[]
    for x in ls2:
            y=str(x)
            ls3.append(y)
    string=','.join(ls3)
    print(string)

