a=eval(input())
b=[]
for x in reversed(a):
    if a.count(x)==1:
        b.append(x)
b.sort()
if len(b)!=0:
    print(*b,sep=",")
else:
    print("False")
