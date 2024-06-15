strs=input() or "ok"
gdp_dict={}
if strs!="ok":
    nation,gdp=strs.split()
    gdp_dict[nation]=gdp
    strs=input().split() or "ok"
nation_list=sorted(list(gdp_dict.keys()))
gdp_list=sorted(list(gdp_dict.values()))
sums=0
for i in gdp_list:
    i=int(i)
    sums+=i
print(nation_list)
print(gdp_list)
if 'India' not in nation_list:
    print("no")
else:
    print("yes")
print(sums)
