GDP={}
while True:
    a=input()
    if a!='ok':
        x,y=a.split()
        GDP[x]=int(y)
    else:
        break
ls1=sorted(list(GDP.keys()))
ls2=sorted(list(GDP.values()))
print(ls1)
print(ls2)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(ls2))




