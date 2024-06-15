a=eval(input())
b=a.copy()
c=[]
for x in b:
    if a.count(x)==1:
        c.append(x)
c.sort()
if c:
    for y in c:
        print(x,end=",")
else:
    print("False")

