gdp = {}
a = input()
while a!= "ok":
    ls1 = a.split(" ")
    gdp[ls1[0]]=ls1[1]
    a = input()    
h = list(gdp.keys())
j = list(gdp.values())
print(h)
print(j)
if "india" in gdp:
    print("ok")
else:
    print("no")
print(sum(j))  


