gdp={}
a,b=input().split()
gdp.update(a,b)

print(gdp[0])
print(gdp[1])
if "india" in gdp:
    print("yes")
else:
    print("no")
print(sum(line[1]))
