info=input()
GDP={}
while info!="ok":
    name=info.split()[0]
    GDP=eval(info.split()[1])
    GDP[name]=GDP

print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print('ok' if 'India' in GDP else 'no' )
print(sum(GDP.values))
