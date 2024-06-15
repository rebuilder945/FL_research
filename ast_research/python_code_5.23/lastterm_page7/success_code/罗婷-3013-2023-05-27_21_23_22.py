country_info={}
countries=[]
gdps=[]
while True:
    info=input()
    if info == "OK":
        break
    country,gdp=info.split()
    gdp=eval(gdp)
    countries.append(country)
    gdps.append(gdp)
    country_info[country]=gdp
countries.sort()
gdps.sort()
print(countries)
print(gdps)
print("yes"if country_info.get('india',None)else"no")
print(sum(gdps))
