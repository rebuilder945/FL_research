ls=eval(input())
ls1=[]
for x in ls:
    if ls.count(x)==1:
        ls1.append(x)
ls1.sort()
if len(ls1)==0:
    print('False')
else:
    print(ls1)
