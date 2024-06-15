gdp={}
a=input()
while a!="ok":
    a,b=map(str,a.split())
    gdp[a]=int(b)
    a=input()
ls1=[]
ls2=[]
for i in gdp.keys():
    ls1.append(i)
for i in gdp.values():
    ls2.append(i)
ls1.sort()
ls2.sort()
print(ls1)
print(ls2)
if "india" in gdp:
    print("no")
else:
    print("no")
print(sum(ls2))

