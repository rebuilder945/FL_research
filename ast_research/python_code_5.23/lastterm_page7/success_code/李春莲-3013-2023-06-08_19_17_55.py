a=input() or "ok"
GDP={}
while(a!="ok"):
    name,g=a.split()
    g=eval(g)
    GDP[name]=g
    a=input() or "ok"
l1=list(GDP.keys())
l2=list(GDP.values())
l1.sort(reverse=False)
l2.sort(reverse=False)
print(l1)
print(l2)
if 'India' in name:
    print('yes')
else:
    print('no')
print(sum(GDP.values()))
