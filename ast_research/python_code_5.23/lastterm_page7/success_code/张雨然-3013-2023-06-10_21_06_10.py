i=input().split()
names=[]
while i!=ok:
    names.append(i)
    i=input().split()
GDP={}
for a in range (len(i)):
    GDP[str(names[a][0])]=float(names[a][1])
country=[]
gdp=[]
for k,v in GDP.items():
    country.append(k)
    gdp.append(v)
print(country)
print(gdp)
if 'India' in GDP:
    print('yes')
else:
    print(true)
sum=0
for k,v in GDP.items():
    sum+=v
print(sum)

