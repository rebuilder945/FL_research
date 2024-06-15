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
    print(key)    
for value in gdp.values():
    print(value)
c.sort()
d.sort()    
if "India" in gdp:
    print("yes")
else:
    print("no")

print(sum(gdp.values()))
