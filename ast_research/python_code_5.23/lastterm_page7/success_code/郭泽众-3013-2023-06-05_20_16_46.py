gdpd = {}
mix = input()
while mix != 'ok':
    coun, gdp = map(str, mix.split(' '))
    gdpd[coun] = int(gdp)
    mix = input()
lst1 = list(gdpd.keys())
lst2 = list(gdpd.values())
print(sorted(lst1))
print(sorted(lst2))
if 'India' in gdpd:
    print("yes")
else:
    print('no')
print(sum(list(gdpd.values())))
