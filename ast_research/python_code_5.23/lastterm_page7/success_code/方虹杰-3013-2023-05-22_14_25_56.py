gdp={}
a=input()
while a!='ok':
    a,f=map(str,a.split(''))
    gdp[a]=int(f)
    a=input()
b=[]
c=[]
for i in gdp.keys():
    b.append(i)
for i in gdp.values():
    c.append()
b.sort()
c.sort()
print(b)
print(c)
if 'India' in gdp:
    print('yes')
else:
    print('no')
print(sum(c))
    

