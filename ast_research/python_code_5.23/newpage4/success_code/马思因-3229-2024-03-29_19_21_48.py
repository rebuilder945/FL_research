n=eval(input())
b=[]
for i in range(len(n)):
    a=n[i]
    c=n.copy()
    c.remove(a)
    if a in c:
        pass
    else:
        b.append(a)
b.sort()
if len(b)==0:
    print("False")
else:
    for i in range(len(b)-1):
        print(b[i],end=',')
    print(b[-1])
