a  =  {}
while True:
    b=input()
    if b!='ok':
        contruy,gdp=b.split()
        a[contruy]=int(gdp)
    else:
        break
newstu=sorted(a.keys())
newstu1=sorted(a.values())
print(newstu)
print(newstu1)
if a.get('india',0)==0:
    print('no')
else:
    print('yes')
print(sum(newstu.values()))
