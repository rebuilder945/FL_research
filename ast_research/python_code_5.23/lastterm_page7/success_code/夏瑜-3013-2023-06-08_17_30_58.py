s=input()
a={}
while s!='ok':
    b=list(s.split(' '))
    a[b[0]]=b[1]
    s=input
n=[]
m=[]
for x in a.keys():
    n.append(x)
for x in a.values():
    m.append(x)
print(n)
print(m)
if "india" in a:
    print("yes")
else:
    print("no")
print(sum(m))


