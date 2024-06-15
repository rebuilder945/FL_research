s = input() or "ok"
GDP = {}
keylist = []
valuelist = []
while s != "ok":
    name,gdp = s.split()[0],eval(s.split()[1])
    GDP[name] = gdp    
    s = input() or "ok"
a = GDP.keys()
keylist = list(a)
print(keylist.sort())
b = GDP.values()
valuelist = list()
print(valuelist.sort())
if "India" in GDP:
    print("yes")
else:
    print("no")
print(sum(valuelist))

