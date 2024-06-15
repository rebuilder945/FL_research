
GDP = {}
while True:
    input_str = input().strip()
    if input_str == "ok":
        break
    else:
        country, gdp = input_str.split()
        GDP[country] = int(gdp)


keys = list(GDP.keys())
keys.sort()

values = list(GDP.values())
values.sort()

if 'India' in GDP:
    print('yes')
else:
    print('no')

sum_values = sum(GDP.values())

print(keys)
print(values)
print(sum_values)
