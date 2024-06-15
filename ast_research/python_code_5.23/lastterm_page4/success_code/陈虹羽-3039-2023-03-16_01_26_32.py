a=eval(input())
b=a.copy()
c=max(a)
for i in a:
    if i==c:
     b.remove(i)
print(b)
