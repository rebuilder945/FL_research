k=input()
m=input()
a=[]
b=[]
for x in k:
    a.append(x)
for x in m:
    b.append(x)
l=a.copy()
i=0
for x in range(len(a)-1):
    if a[x]==b[0]:
        if len(a)>=x+len(b):
            if a[x:x+len(b)]==b:
                del l[x-i:x+len(b)-i]
                i=i+len(b)
print(''.join(l))
