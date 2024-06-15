s=input()
GDP={}
while s!='ok':
    ls=s.split()
    GDP[ls[0]]=int(ls[1])
    s=input()
b=list(GDP.keys())
b.sort()
a=list(GDP.values())
print(b)
a.sort()
print(a)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(a))

