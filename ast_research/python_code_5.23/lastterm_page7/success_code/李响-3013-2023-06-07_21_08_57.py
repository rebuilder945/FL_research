a = []
GDP = {}
while input() != 'ok':
    name = input().split()[0]
    gdp = eval(input().split()[1])
    GDP[name] = gdp
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print('yes'if'India' in GDP else 'no')
print(sum(GDP.values()))
