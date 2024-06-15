GDP = {}
while True:
        shuru = input()
        if shuru == 'ok':
                break
        country,gdp = shuru.split()
        GDP[country]  = int(gdp)

keys = sorted(list(GDP.keys()))
values = sorted(list(GDP.values()))
sum_v = sum(values)

print(keys)
print(values)
if 'India' in GDP:
        print('yes')
else:
        print('no')
print(sum_v)
