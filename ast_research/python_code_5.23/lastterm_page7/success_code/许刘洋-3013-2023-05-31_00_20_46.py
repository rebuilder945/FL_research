GDP={}
s=input()
while s!="ok":
    s=list(s.split())
    GDP[s[0]]=s[1]
    s=input()
b=list(GDP.keys())
b.sort()
c=list(GDP.values())
d=list(map(eval,c))
d.sort()
print(b)
print(d)
if "india" in b:
    print("yes")
else:
    print("no")
print(sum(d))
