a=eval(input())
b=[]
for i in a:
    if a.count(i)>1:
        for x in range(a.count(i)):
            a.remove(i)
if len(a)>0:
    a.sort()
    b=','.join(str(x) for x in a)
    print(b)
else:
    print("False")
