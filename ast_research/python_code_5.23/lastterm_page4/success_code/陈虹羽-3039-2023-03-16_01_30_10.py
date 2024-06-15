a=eval(input())
b=a.copy()
c=max(a)
e=min(a)
for i in a:
    if i==c or i==e:
      b.remove(i)
print(b)
