
a  =  {}
while True:
    b=input()
    if b!='ok':
        contruy,gdp=b.split()
        a[contruy]=int(gdp)
    else:
        break
newstu=dict(sorted(a.items(),key=lambda x:x[1]))
print(list(newstu.keys()))
print(list(newstu.values()))
if newstu.get('india',0)==0:
    print('no')
else:
    print('yes')
print(sum(newstu.values()))
