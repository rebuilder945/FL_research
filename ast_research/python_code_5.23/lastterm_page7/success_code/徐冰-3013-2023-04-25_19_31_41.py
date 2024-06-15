GDP={}
a=input().split()
while a!=["ok"]:
    GDP[a[0]]=eval(a[1])
    a=input().split()
ls1=sorted(list(GDP.keys()))
ls2=sorted(list(GDP.values()))
print(ls1)
print(ls2)
if 'India' in ls1:
    print("yes")
else:
    print("no")
print(sum(ls2))
