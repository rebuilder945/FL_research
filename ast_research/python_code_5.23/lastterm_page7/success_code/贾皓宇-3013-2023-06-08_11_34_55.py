dic={}
while True:
    i=input()
    if i=='ok':
        break
    else:
        a=list(i.split())
        a[1]=int(a[1])
        dic[a[0]]=a[1]
guojia=list(dic.keys())
gdp=list(dic.values())
guojia.sort()
gdp.sort()
print(guojia)
print(gdp)
if 'India' in dic:
    print('yes')
else:
    print('no')
print(sum(gdp))
