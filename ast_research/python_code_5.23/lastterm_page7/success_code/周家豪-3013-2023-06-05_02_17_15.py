lst=input()
gdp={}
while lst!='ok':
    a,b=lst.split(' ')
    gdp[a]=eval(b)
    lst=input()
lst1=list(gdp.keys())
lst2=list(gdp.values())
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if gdp.get('India'):
    print('yes')
else:
    print('no')
print(sum(lst2))
