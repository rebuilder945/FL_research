a=eval(input())
b=[]
for x in a:
    if a.count(x)==1:
        b.append(x)
if len(b)==0:
    print("False")
else:
    b.sort()
    print(b)
