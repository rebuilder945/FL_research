GDP={}
s=input()
while s!="ok":
    s=list(s.split())
    GDP[s[0]]=s[1]
    s=input()
b=list(GDP.keys())
b.sort()
c=list(GDP.values())
c.sort()
print(b,c)
if "india" in b:
    print("yes")
else:
    print("no")
print(sum(map(eval,c)))
