a=eval(input())
b=a.copy()
c=a.count(0)
for i in a:
    if i==0:
        b.remove(i)
        b.append(i)
print(b)
