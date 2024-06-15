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
    print("yes")
else:
    print("no")
for i in range(len(j)):
    j[i] = int(j[i])
print(sum(j)) 


