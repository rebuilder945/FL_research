gdp={}
while True:
    a=input()
    if a =="ok":
        break
    lst=a.split()
    gdp[lst[0]]=int(lst[1])
print(sorted(list(gdp.keys())))
print(sorted(list(gdp.values())))
if "India" in gdp:
    print("yes")
else:
    print("no")
print(sum(list(gdp.values())))







            
