a=eval(input())
b=a.copy()
for i in a:
    if a.count(i)>1:
        c=a.count(i)
        for x in range(c):
            b.remove(i)
if len(b)==0:
    print(False)
else:
    for i in b:
        print(i,end=',')


