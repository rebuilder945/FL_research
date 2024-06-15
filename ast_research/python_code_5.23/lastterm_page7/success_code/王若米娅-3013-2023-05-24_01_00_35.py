a=input()
coun_gdp={}
while (a!="ok"):
    a=a.split()
    country=a[0]
    gdp=int(a[1])
    coun_gdp[country]=gdp
    str1=input()
ls=list(coun_gdp.values())
ls1=list(coun_gdp.keys())
ls.sort()
ls1.sort()
print(ls1)
print(ls)

if "India" not in ls1:
    print("no")
else:
    print("yes")
print(sum(ls))
