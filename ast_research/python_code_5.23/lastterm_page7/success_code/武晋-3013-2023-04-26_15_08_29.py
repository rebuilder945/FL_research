GDP={}
countries=[]
values=[]
while True:
    ls= input()
    if ls =="ok":
        break
    else:
        ls=list(ls.split(" "))
        GDP[ls[0]]=ls[1]
for x,y in GDP.items():
    countries.append(x)
    values.append(int(y))
    countries.sort()
    values.sort()
print(countries)
print(values)
if "India" in GDP:
    print("yes")
else:
    print("no")
print(sum(values))
