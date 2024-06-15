a = []
GDP = {}
while True:
    i = input()
    if i =='ok':
        break
    a.append(i)
    name = a[0]
    gdp = eval(a[1])
    GDP[name] = gdp
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print('yes'if'India' in GDP else 'no')
print(sum(GDP.values()))
