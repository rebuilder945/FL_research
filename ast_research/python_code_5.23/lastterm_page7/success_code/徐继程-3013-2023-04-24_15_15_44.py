item=input()or"ok"
GDP={}
while(item!="q"):
    name,gdp=item.split()
    gdp=eval(gdp)
    GDP.update({name:gdp})
    item=input()or"ok"
print(list(GDP.keys).sort(reverse=True))
print(list(GDP.values).sort(reverse=True))
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(list(GDP.values)))
