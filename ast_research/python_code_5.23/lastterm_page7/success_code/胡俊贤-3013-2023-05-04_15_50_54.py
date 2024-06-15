s=input()
GDP={}
while s!='ok':
    ls=s.split()
    GDP[ls[0]]=ls[1]
    s=input()
a=list(GDP.values()).sort()
print(list(GDP.keys()).sort)
print(a)
print('India' in GDP)
print(sum(list(a)))

