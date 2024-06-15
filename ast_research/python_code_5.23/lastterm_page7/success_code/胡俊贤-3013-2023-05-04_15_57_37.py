s=input()
GDP={}
while s!='ok':
    ls=s.split()
    GDP[ls[0]]=int(ls[1])
    s=input()
a=list(GDP.values())
print(list(GDP.keys()).sort)
a.sort()
print(a)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(a))

