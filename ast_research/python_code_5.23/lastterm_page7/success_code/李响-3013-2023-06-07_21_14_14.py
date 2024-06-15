GDP = {}
a = []
while input() != 'ok':
    name = a[0]
    gdp = eval(a[1])
    GDP[name] = gdp
    a = input().split()
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print('yes'if'India' in GDP else 'no')
print(sum(GDP.values()))
