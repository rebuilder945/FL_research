info=input()
GDP={}
while info!="ok":
    name,gdp=info.split()[0],
    GDP[name]=gdp
    info=input()
print(sorted(list(GDP.kesy())))
print(sorted(list(GDP.values())))
print("yes"if "India"in GDP else"No")
print(sum(GDP.values()))

