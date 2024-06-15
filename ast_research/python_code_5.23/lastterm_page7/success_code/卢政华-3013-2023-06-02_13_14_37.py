gdp={}
a, b = input().split()
gdp[a] = b
for key in gdp:
    print(key)
for value in gdp:
    print(value)

if "India" in gdp:
    print("yes")
else:
    print("no")
print(int(b))
