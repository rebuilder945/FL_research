GDP={}
while True:
    line=input()
    if line == "ok":
        break
    country,gdp=line.split()
    GDP[country]=gdp
ls1=list(GDP.keys())
ls2=list(GDP.values())
print(ls1)
print(ls2)
if "India" in GDP.keys():
    print("yes")
else:
    print("no")
print(sum(ls2))

