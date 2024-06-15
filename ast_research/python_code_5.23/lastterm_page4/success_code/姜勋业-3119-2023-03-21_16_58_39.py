a=eval(input())
for i in a[0:len(a)]:
    z=a.count(i)
    for x in range(z-1):
        a.remove(i)
print(a)
