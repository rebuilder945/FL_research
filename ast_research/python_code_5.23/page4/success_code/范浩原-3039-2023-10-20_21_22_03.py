a=eval(input())
b=max(a)
c=min(a)
a1=a.copy()
for x in a:
    if x==b or x==c:
        a1.remove(x)
print(a)
