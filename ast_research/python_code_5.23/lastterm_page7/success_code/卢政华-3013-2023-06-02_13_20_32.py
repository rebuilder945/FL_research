gdp={}
a, b = input().split()
gdp[a] = b
for key in gdp.keys():
    print(key)
for value in gdp.values():
    print(value)

if "India" in gdp:
    print("yes")
else:
    print("no")
print(int(b))
