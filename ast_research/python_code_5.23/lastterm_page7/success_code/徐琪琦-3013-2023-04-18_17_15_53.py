s = input() or "ok"
GDP = {}
keylist = []
valuelist = []
while s != "ok":
    name,gdp = s.split()[0],eval(s.split()[1])
    GDP[name] = gdp    
    s = input() or "ok"
keylist = list(GDP.keys())
print(keylist)
valuelist = list(GDP.values)
print(valuelist)
if "India" in GDP:
    print("yes")
else:
    print("no")
print(sum(valuelist))

