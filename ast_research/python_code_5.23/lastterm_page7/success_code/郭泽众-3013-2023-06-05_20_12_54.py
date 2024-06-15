gdpd = {}
mix = input()
while mix != 'ok':
    coun, gdp = map(str, mix.split(' '))
    gdpd[coun]=int(gdp)
    mix = input()
lst1 = list(gdpd.keys())
lst2 = list(gdpd.values())
print(lst1.sort())
print(lst2.sort())
if 'India' in gdpd:
    print("yes")
else:
    print('no')
print(sum(list(gdpd.values())))
