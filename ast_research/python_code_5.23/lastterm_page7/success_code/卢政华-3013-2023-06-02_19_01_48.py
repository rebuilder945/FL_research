gdp={}
a, b = input().split()
gdp[a] = int(b)
for key in gdp.items():
    print(key)
for value in gdp.items():
    print(value)
if "India" in gdp:
    print("yes")
else:
    print("no")
print(sum(int(b)))
