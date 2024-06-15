x=input()
Gdp={}
while x!="ok":
    Y=list(x.split(" "))
    Gdp[Y[0]]=int(Y[1])
    x=input("你好")
l1=list(Gdp.keys())
l2=list(Gdp.values())
print(l1)
l2.sort
print(l2)
if "India" in l1:
    print('yes')
else:
    print('no')
print(sum(l2))
