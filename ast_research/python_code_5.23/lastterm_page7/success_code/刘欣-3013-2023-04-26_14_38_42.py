nation,gdp=input().split() or "ok"
if nation !="ok" and gdp!="ok":
    gdp_dict=dict(zip(nation,gdp))
    nation,gdp=input().split() or "ok"
nation_list=sorted(list(gdp_dict.keys()))
gdp_list=sorted(list(int(gdp_dict.values())))
print(nation_list)
print(gdp_list)
if 'India' not in nation_list:
    print("no")
else:
    print("yes")
sums=sum(gdp_list)
print(sums)
