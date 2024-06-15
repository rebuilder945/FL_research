gdp={}
while True:
    a=input()
    if a =="ok":
        break
    lst=a.split()
    gdp[lst[0]]=float(lst[1])
print(list(gdp.keys()))
print(list(gdp.values()))
if "india" in gdp:
    print("yes")
else:
    print("no")
print(sum(list(gdp.values())))







            
