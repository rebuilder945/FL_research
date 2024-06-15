a=eval(input())
b=a.count(0)
for i in a:
    if i==0:
        a.remove(i)
for i in range(b):
    a.append(0)
print(a)


