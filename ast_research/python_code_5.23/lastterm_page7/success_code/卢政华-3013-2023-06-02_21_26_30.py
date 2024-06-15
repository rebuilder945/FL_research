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
    
for value in gdp:
    d.append(value)
    
if "India" in gdp:
    print("yes")
else:
    print("no")
sums=sum(list(b))
print(c)
print(d)
print(sums)
