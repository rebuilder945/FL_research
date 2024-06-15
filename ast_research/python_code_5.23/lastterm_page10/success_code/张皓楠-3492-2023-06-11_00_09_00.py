a=[]
b=[]
m=list(input())
for i in m:
    if i not in a:
        a.append(i)
if a!=m:
    for i in m:
        if m.count(i)==1:
            b.append(i)
    print(b[0])
else:
    print('None')


