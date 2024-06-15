a=eval(input())
b=max(a)
c=min(a)
d=a.copy()
for i in a:
    if i==b or i==c:
        a.remove(i)
        continue
print(a)
