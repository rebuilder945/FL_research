k=input()
m=input()
a=[]
b=[]
for x in k:
    a.append(x)
for x in m:
    b.append(x)
l=a.copy()
for x in range(len(a)-1):
    if a[x]==b[0]:
        if len(a)>=x+len(b):
            if a[x:x+len(b)]==b:
                for t in a[x:x+len(b)]:
                    l.remove(t)
print(''.join(l))
