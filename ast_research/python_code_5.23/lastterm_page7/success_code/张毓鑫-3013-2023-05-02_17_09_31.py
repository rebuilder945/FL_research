a=input()
b=a.split(' ')
c={}
while b[0]!='ok':
    c[b[0]]=b[1]
    a=input()
    b=a.split(' ')
a1=list(c.keys())
a2=list(c.values())
print(a1.sort())
print(a2.sort())
if 'India' in c.keys():
    print('yes')
else:
    print('no')
d=list(c.values())
e=0
for i in d:
    e+=int(i)
print(e)
