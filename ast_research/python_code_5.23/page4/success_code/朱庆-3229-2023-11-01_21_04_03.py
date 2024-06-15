a = eval(input())
b = []
for x in a:
    if a.count(x)==1:
        b.append(x)
if len(b)>0:
    b.sort()
    b=','.join(str(i) for i in b)
    print(b)
else:
    print(False)    


