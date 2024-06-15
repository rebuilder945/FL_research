
gdp={}
s=input()
while s!='ok':
    s,m=map(str,s.split(' '))
    gdp[s]=m
    s=input()
lst1=gdp.keys()
lst2=gdp.values()
print(lst1)
print(lst2)
if 'India' in gdp:
    print("yes")
else:
    print("no")
aaa=sum(int(lst2))
print(aaa)


