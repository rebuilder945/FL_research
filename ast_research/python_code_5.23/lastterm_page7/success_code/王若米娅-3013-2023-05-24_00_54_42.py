str1=input()
coun_gdp={}
while (str1!="ok"):
    country, gdp=input.split(" ")
    gdp=eval(gdp)
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
