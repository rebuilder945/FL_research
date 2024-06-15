
gdp={}
s,m=input()
while s!='ok':
    gdp[s]=m
    s,m=input()
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


