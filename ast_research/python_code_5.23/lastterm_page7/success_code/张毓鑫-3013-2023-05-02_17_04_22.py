a=input()
b=a.split(' ')
c={}
while b[0]!='ok':
    c[b[0]]=b[1]
    a=input()
    b=a.split(' ')
print(list(c.keys()))
print(list(c.values()))
if 'India' in c.keys():
    print('yes')
else:
    print('no')
d=sum(list(c.values()))
print(d)
