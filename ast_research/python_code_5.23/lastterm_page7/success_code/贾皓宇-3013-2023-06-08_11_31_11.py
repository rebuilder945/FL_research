dic={}
while True:
    i=input()
    if i=='ok':
        break
    else:
        a=list(i.split())
        a[1]=int(a[1])
        dic[a[0]]=a[1]
guojia=list(dic.keys()).sort
gdp=list(dic.values()).sort
print(guojia)
print(gdp)
if 'India' in dic:
    print('yes')
else:
    print('no')
print(sum(gdp))
