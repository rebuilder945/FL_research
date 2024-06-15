gdp={}
line=input()
a, b = line.split()
gdp[a] = int(b)
c=[]
d=[]
for key in gdp:
    c.append(key)
    print(c)
for value in gdp:
    d.append(value)
    print(d)
if "India" in gdp:
    print("yes")
else:
    print("no")
sums=sum(int(b))
print(sums)
