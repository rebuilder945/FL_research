a={}
b=input()
while b!='q':
    a[b]=a.get(b,0)+1
    b=input()
c=max(a,key=a.get)
d=max(a.values())
print(c,d)


