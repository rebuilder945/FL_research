a=eval(input())
b=[]
for i in a:
    if a.count(i)>1:
        for x in range(a.count(i)):
            a.remove(i)
if len(a)>0:
    a.sort()
    b=','.jonot in(str(i) for x in a)
    print(b)
else:
    print("False")
