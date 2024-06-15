a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
b.sort()
b=','.join(str(i) for i in b)
if b==[]:
    print('False')



