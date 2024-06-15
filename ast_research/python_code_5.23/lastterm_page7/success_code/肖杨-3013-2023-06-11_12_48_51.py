a=input()
GDP={}
while a!='ok':
    b=list(a.split())
    GDP[b[0]]=GDP.get(b[0],0)+int(b[1])
    a=input()
c=list(GDP)
d=[]
for i in c:
    d.append(GDP[i])
c.sort()
d.sort()
print(c)
print(d)
if 'India' in c:
    print('yes')
else:
    print('no')
print(sum(d))




