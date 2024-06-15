a=input()
b=a.split(' ')
c={}
while b[0]!='ok':
    c[b[0]]=b[1]
    a=input()
    b=a.split(' ')
print(list(c.keys()).sort())
print(list(c.values()).sort())
if 'India' in c.keys():
    print('yes')
else:
    print('no')
d=list(c.values())
e=sum(d)
print(e)
