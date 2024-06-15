a=eval(input())
a.sort()
min=a[0]
max=a[-1]
while min in a:
    a.remove(min)
while max in a:
    a.remove(max)
print(a)


