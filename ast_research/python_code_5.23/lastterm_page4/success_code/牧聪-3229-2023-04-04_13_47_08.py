a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
b.sort()
if b==[]:
    print(False)
else:
    print(','.join(map(str, b)) )

