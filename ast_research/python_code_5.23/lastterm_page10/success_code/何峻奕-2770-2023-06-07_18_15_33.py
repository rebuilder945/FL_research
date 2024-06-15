a=input()
b=input()
c=[]
d=[]
for i in a:
    c.append(i)
for x in b:
    d.append(x)
l1=c.sort()
l2=d.sort()
if len(c)!=len(d):
    print("False")
else:    
    if l1==l2:
        print("True")
    else:
        print("False")
