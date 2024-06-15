s=input()
GDP={}
while s!="ok":
    name=s.split()[0]
    gdp=eval(s.split()[1])
    GDP[name]=gdp
    s=input()
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
print('yes' if "india" in GDP else "no")
print(sum(GDP.values()))

