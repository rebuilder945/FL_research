s=input()
GDP={}
while s!='ok':
    a,b=s.split()[0],eval(s.split()[1])
    GDP[a]=b
    s=input()
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print('yes' if 'India' in GDP else 'no')
print(sum(GDP.values()))

