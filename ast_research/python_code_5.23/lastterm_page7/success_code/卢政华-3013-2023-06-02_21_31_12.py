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
for value in gdp.values():
    d.append(value)
c.sort()
d.sort()
print(c)
print(d)    
if "India" in gdp:
    print("yes")
else:
    print("no")

print(sum(gdp.values()))
