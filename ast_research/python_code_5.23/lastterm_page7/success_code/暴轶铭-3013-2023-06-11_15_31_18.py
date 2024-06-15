GDP = {}
a = input()
while a != "ok":
    name, gdp = a.split(" ")
    GDP[name] = int(gdp) 
    a = input()
b = list(GDP.keys())
c = list(GDP.values())
summ = sum(GDP.values()) / len(GDP)
print(b)
print(c)
if "India" in GDP:
    print("yes")
else:
    print("no")
print(int(summ))
