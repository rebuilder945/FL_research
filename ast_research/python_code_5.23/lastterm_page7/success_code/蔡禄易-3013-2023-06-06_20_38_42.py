gdp = {}
a = input()
while a!= "ok":
    ls1 = a.split(" ")
    gdp[ls1[0]]=ls1[1]
    a = input()    
h = list(gdp.keys())
j = list(gdp.values())
h.sort()
j.sort()
print(h)
for i in range(len(j)):
    j[i] = int(j[i])
print(j)
if "India" in h:
    print("yes")
else:
    print("no")
print(sum(j)) 


