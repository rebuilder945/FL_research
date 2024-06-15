a=eval(input())
b=a.count(0)
for i in a:
    if i==0:
        a.remove(i)
c=b-1
for i in range(c):
    a.append(0)
print(a)


