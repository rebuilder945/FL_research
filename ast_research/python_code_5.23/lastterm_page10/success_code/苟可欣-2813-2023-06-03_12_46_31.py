k=input()
b=input()
a=[]
for x in k:
    a.append(x)
for x in range(len(a)):
    if a[x]==b[0]:
        if a[x:x+len(b)]==b:
            del a[x:x+len(b)]
print(''.join(a))
