GDP={}
while True:
    go=input()
    if go=='ok':
        break
    else:
        name,mon=go.split()
        GDP[name]=int(mon)

keys=sorted(GDP.keys())
values=sorted(GDP.values())
total=sum(values)
print(keys)
print(values)
if "India" in GDP:
    print('yes')
else:
    print("no")
print(total)
