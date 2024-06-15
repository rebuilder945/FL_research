gdp={}
a, b = input().split()
gdp[a] = b
print(gdp.get(a))
print(gdp.get(b))
if "India" in gdp:
    print("yes")
else:
    print("no")
print(int(b))
