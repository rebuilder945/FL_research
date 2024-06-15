ls1=[]
ls2=[]
item=input() or "ok"
while item!="ok":
    cou,gdp=input().split( )
    ls1.append(cou)
    ls2.append(int(gdp))
print(ls1)
print(ls2)
if 'India' in ls1:
    print("yes")
else:
    print("no")
print(sum(ls2))
