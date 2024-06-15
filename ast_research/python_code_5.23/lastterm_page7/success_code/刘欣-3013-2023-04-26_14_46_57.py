gdp_dict = {}
while True:
    input_str = input()
    if input_str == 'ok':
        break
    k, v = input_str.split(' ')
    gdp_dict[k] = int(v)
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
