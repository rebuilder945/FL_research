a=input()
b=input()
c=''
o=len(b)
for d in a:
    if a[a.index(d):a.index(d)+len(b)] != b :
        c+=d
print(c)
