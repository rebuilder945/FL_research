a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
    else:
        continue
if len(b)>0:
    b.sort()
    b=','.join(str(y) for y in b)
    print(b)
else:
    print("False")



