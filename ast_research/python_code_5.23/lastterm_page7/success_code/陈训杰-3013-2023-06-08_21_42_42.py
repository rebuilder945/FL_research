GDP={}
while True:
    s=input()
    if s=="ok":
        break
    a,b=s.split()
    b=eval(b)
    GDP[a]=b
country=[]
gdp=[]
for k,v in GDP.items():
    country.append(k)
    gdp.append(v)
country.sort()
gdp.sort()
print(country)
print(gdp)
if 'India' in country:
    print('yes')
else:
    print('no')
print(sum(gdp))
