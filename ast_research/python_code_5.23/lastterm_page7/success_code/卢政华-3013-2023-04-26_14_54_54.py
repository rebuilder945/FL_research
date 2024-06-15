gdp = {}
item = input()
while item != 'ok':
    country, gdp = item.split()
    gdp[country] = int(gdp)
    item = input()

keys_list = sorted(list(gdp.keys()))
values_list = sorted(list(gdp.values()))

if 'india' in gdp:
    print('yes')
else:
    print('no')

total_gdp = sum(gdp.values())
print(keys_list)
print(values_list)
print(total_gdp)
