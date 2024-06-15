a=eval(input())
b=max(a)
c=min(a)
l=a.copy()
for i in a:
    if i==b or i==c:
        l.remove(i)
    else:
        continue
print(l)

        







