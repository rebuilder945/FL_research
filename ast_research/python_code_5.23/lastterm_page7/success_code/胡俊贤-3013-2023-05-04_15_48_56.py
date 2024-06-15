s=input()
GDP={}
while s!='ok':
    ls=s.split()
    GDP[ls[0]]=ls[1]
a=list(GDP.values())
print(list(GDP.keys))
print(a)
print('India' in GDP)
print(sum(list(a)))

