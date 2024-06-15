a=input()
b=a.split(' ')
c={}
while b[0]!='ok':
    c[b[0]]=b[1]
    a=input()
    b=a.split(' ')
print(c.keys())
print(c.values())
if 'India' in c.keys():
    print('yes')
else:
    print('no')
d=sum(c.values())
print(d)
