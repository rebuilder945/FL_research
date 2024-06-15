info=input()
GDP={}
while info!="ok":
    name,gdp=info.split()[0],eval(info.split()[1])
    GDP[name]=gdp
    info=input()
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print("yes"if "India"in GDP else"No")
print(sum(GDP.values()))

