li=eval(input())
n=max(li)
m=min(li)
li1=li.copy()
for x in li:
    if x==n or x==m:
        li1.remove(x)
print(li1)
