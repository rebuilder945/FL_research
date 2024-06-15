a={}
s=list(input())
while s!="ok"
    a[s[0]]=s[1]
    s=list(input())
b=list(a.keys())
b.sort()
c=list(a.values())
c.sort()
print(b,c)
if "india" in a:
    print("yes")
else:
    print("no")
print(sum(c))
