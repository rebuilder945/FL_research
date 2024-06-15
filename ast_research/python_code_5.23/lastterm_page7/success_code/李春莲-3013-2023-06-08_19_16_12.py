a=input() or "ok"
GDP={}
while(a!="ok"):
    name,g=a.split()
    g=eval(g)
    GDP[name]=g
    a=input() or "ok"
l1=list(GDP.keys())
l2=list(GDP.values())
print(l1.sort())
print(l2.sort())
if 'India' in name:
    print('yes')
else:
    print('no')
print(sum(GDP.values()))
