dic = {}
while True:
    data = input()
    if data == "ok":
        break
    else:
        country, gdp = data.split()
        dic[country] = int(gdp)

keys = sorted(dic.keys())
print(keys)

values = sorted(dic.values())
print(values)

if "India" in dic:
    print("yes")
else:
    print("no")

total_gdp = sum(dic.values())
print(total_gdp)

