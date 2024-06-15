GDP={}
s=""
while s!="ok":
    a=input().split()
    if a[0]!="ok":
        GDP[a[0]]=a[1]
    s=a[0]
print(sorted(list(GDP.keys())))
print(sorted(map(int,list(GDP.values()))))
if "India" not in GDP.keys():
    print("no")
else:
    print("yes")
print(sum(map(int,list(GDP.values()))))     




