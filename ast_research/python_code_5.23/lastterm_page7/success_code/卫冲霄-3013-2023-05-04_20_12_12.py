GDP={}
user_input=input().split()
while user_input !="ok":
    nation,gdp=user_input
    GDP[nation]=int(gdp)
    user_input=input()
ls1=list(GDP.key())
ls2=list(GDP.value())
print(ls1)
print(ls2)
print("yes" if "India" in ls1 else "no")
print(sum(ls2))
