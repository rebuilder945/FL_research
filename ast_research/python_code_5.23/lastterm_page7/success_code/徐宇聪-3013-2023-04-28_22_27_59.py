GDP ={}
while True:
    line = input().strip()
    if line == 'ok':
        break
    country,gdp = line.split()
    GDP[country] = int(gdp)

keys = sorted(list(GDP.keys()))
values = sorted(list(GDP.values()))
print(keys)
print(values)
if 'India' in GDP:
    print('yes')
else:
    print('no')

print(sum(GDP.values()))
