a=eval(input())
b=a.copy()
for i in a:
    d=i
    if a.count(i)>1:
        c=a.count(i)
        for i in range(c):
            b.remove(d)
if len(b)==0:
    print(False)
else:
    for i in b:
        print(i,end=',')


