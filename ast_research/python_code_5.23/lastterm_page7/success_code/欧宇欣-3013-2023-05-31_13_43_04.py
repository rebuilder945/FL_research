gdp={}
a=input()
while a!='ok':
    a,b=map(str,a.split(' '))
    gdp[a]=int(b)
    a=input()
lst1=[]
lst2=[]
for i in gdp.keys():
    lst1.append(i)
for i in gdp.values():
    lst2.append(i)
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' in gdp:
    print('yes')
else:
    print('no')
print(sum(lst2))

