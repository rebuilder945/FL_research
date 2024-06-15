GDP={}
while True:
    s=input()
    if s == "ok":
        break
    else:
        s=s.split()
        GDP[s[0]]=int(s[1])
y1=list(GDP.keys())
y2=list(GDP.values())
y1.sort()
y2.sort()
y11=list(str(x) for x in y1)
y12=list(int(x) for x in y2)

sum=0
for v in GDP.values():
    sum+=int(v)
print(y1)
print(y2)
if GDP.get("India")==None:
    print("no")
else:
    print("yes")
print(sum)
