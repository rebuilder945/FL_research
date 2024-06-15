i=input().split()
names=[]
while i!=['ok']:
    names.append(i)
    i=input().split()
GDP={}
for a in range (len(names)):
    GDP[str(names[a][0])]=int(str((names[a][1])))
country=[]
gdp=[]
for k,v in GDP.items():
    country.append(k)
    gdp.append(v)
c2=country.sort()
g2=gdp.sort()
print(c2)
print(g2)
if 'India' in GDP:
    print('yes')
else:
    print("no")
sum=0
for k,v in GDP.items():
    sum+=v
print(sum)

