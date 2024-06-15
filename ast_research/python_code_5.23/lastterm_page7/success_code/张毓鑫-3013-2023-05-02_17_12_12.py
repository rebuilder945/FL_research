a=input()
b=a.split(' ')
c={}
while b[0]!='ok':
    c[b[0]]=int(b[1])
    a=input()
    b=a.split(' ')
a1=list(c.keys())
a2=list(c.values())
a1.sort()
a2.sort()
print(a1)
print(a2)
if 'India' in c.keys():
    print('yes')
else:
    print('no')
d=list(c.values())
e=0
for i in d:
    e+=int(i)
print(e)
