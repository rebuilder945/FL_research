info=input()
GDP={}
while info!="ok":
    name=info.split()[0]
    gdp=eval(info.split()[1])
    GDP[name]=gdp
    info=input()
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print("yes" if "India" in GDP else "no")
print(sum(GDP.values()))

