GDP={}
s=input()
if s!='ok':
    name=s.split()[0]
    gdp=eval(s.split()[1])
    GDP['name']=gdp
print(list(sorted(GDP.keys())))
print(list(sorted(GDP.values())))
print('yes'if 'India'in GDP else'not')
print(sum(GDP.values()))
