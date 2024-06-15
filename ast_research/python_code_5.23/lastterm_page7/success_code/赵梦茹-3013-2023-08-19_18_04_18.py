gdp={}
a=input()
while a!="ok":
    a,b=map(str,a.split())
    gdp[a]=eval(b)
    a=input()
k=[]
v=[]
for i in gdp.keys():
    k.append(i)
for i in gdp.values():
    v.append(i)
k.sort()
v.sort()
print(k)
print(v)
if "India" in gdp:
    print("yes")
else:
    print("no")
print(sum(v))
