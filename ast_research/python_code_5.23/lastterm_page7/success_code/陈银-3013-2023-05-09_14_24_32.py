gdp = {}
country = []
money = []
while True:
    a = input()
    if a == "ok":
        break
    country1,money1 = a.split()
    country.append(country1)
    money.append(int(money1))
    gdp[country1] = int(money1)
country.sort()
money.sort()
print(country)
print(money)
if "India" in country:
    print("yes")
else:
    print("no")
print(sum(gdp.values()))
