item=input() or "ok"
countryGDP={}
while(item!="ok"):
        country,GDP=item.split()
        GDP=int(GDP)
        country[GDP]=GDP
        item=input() or "ok"
countrylist=list(countryGDP.keys())
GDPlist=list(countryGDP.values())
print(countrylist)
print(GDPlist)
if 'India' in countrylist:
    print('yes')
else:
    print('no')
print(sum(GDPlist))




