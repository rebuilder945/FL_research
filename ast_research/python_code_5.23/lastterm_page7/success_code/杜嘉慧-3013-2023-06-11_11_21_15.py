GDP={}
s=input()
while s!='ok':
    name=s.split()[0]
    gdp=eval(s.split()[1])
    GDP[name]=gdp
    s=input()
print(list(sorted(GDP.keys())))
print(list(sorted(GDP.values())))
print('yes'if 'India'in GDP else'no')
print(sum(GDP.values()))
