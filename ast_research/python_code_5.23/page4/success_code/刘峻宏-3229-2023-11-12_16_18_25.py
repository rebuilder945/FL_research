a=eval(input())
b=[]
c=[]
for i in range(len(a)):
    if not a[i] in b :
        b.append(a[i])
for i in range (len(b)):
    a.remove(b[i])
for i in range(len(b)):
    if not b[i] in a:
        c.append(str(b[i]))

if c==[]:
    print("False")
else:
    c.sort()
    print(",".join(c))
