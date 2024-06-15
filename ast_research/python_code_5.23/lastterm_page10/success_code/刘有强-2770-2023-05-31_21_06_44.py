a=str(input())
e=str(input())
b=[]
d=[]
for x in a:
    if x not in b:
        b.append(x)
for i in e:
    if i not in d:
        d.append(i)
c = sorted(b)
q = sorted(d)
if c == q:
    print("True")
else:
    print("False")
