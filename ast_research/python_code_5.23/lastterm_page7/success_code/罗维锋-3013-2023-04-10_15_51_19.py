GDP={}
s=""
while s!="ok":
    a=input().split()
    if a[0]!="ok":
        GDP[a[0]]=a[1]
    s=a[0]
print(list(GDP.keys()))
print(list(GDP.values()))
if "India" not in GDP.keys():
    print("no")
print(sum(list(GDP.values())))     

