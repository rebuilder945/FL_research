a=input()
b=input()
c=[]
d=[]
for i in a:
    c.append(i)
for i in b:
    d.append(i)
c.sort()
d.sort()
if c==d:
    print("True")
else:
    print("False")
