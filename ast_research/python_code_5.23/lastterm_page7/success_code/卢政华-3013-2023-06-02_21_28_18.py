gdp={}
while True:
    line = input()
    if line == "ok":
        break
    a, b = line.split(" ")
    gdp[a] = int(b)
gdp[a] = int(b)
c=[]
d=[]
for key in gdp:
    c.append(key)
    
for b in gdp:
    d.append(b)
    
if "India" in gdp:
    print("yes")
else:
    print("no")
print(c)
print(d)
print(sum(gdp.values))
