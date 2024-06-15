GDP = {}
while True:
    a=input().split()
    if a[0]=='ok':
        break
    else:
        country = a[0]
        gdp = int(a[1])
        GDP[country] = gdp

keys = list(GDP.keys())
keys.sort()
print(keys)
values = list(GDP.values())
values.sort()
print(values)
if 'India' in GDP:
    print('yes')
else:
    print("no")

total_gdp = sum(GDP.values())
print(total_gdp)

