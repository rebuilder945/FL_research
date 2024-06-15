data=input()
dic={}
country=[]
GDP=[]
while data!='ok':
    lst=data.split()
    country.append(lst[0])
    GDP.append(int(lst[-1]))
    data=input()
country.sort()
GDP.sort()
print(country)
print(GDP)
if 'India' in country:
    print('yes')
else:
    print('no')
he=sum(GDP)
print(he)
