GDP={}
while True:
    a=input().split(" ")
    if a==["ok"]:
        break
    else:
        GDP[a[0]]=int(a[1])
ls=[x for x in GDP.keys()]
ls2=[y for y in GDP.values()]
ls.sort()
ls2.sort()
print(ls)
print(ls2)
if 'india' in GDP.keys() or 'India' in GDP.keys():
    print("yes")
else:
    print('no')
print(sum(GDP.values()))
