GDP = {}
a = input()
while a != "ok":
    name, gdp = a.split(" ")
    GDP[name] = int(gdp) 
    a = input()
b = list(GDP.keys())
b.sort()
c = list(GDP.values())
c.sort()
summ = sum(GDP.values())
print(b)
print(c)
if "India" in GDP:
    print("yes")
else:
    print("no")
print(int(summ))
