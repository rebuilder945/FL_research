gdp={}
a=input()
while a!="ok":
    a,b=a.split(' ')
    gdp[a]=eval(b)
    a=input()
lst1=[]
lst2=[]
for i in gdp.keys():
    lst1.append(i)
print(lst1.sort())
for i in gdp.values():
    lst2.append(i)
print(lst2.sort())
if 'India' in gdp.keys():
    print('yes')
else:
    print('no')
print(sum(lst2))
