a=input() or "ok"
GDP={}
while(a!="ok"):
    name,g=a.split()
    g=eval(g)
    GDP[name]=g
    a=input() or "ok"
print(list(GDP.keys()))
print(list(GDP.values()))
if 'India' in name:
    print('yes')
else:
    print('no')
print(sum(GDP.values()))
