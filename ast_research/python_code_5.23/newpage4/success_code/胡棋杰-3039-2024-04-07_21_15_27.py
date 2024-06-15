a=eval(input())
x=sorted(a)
min=x[0]
max=x[-1]
while min in a:
    a.remove(min)
while max in a:
    a.remove(max)
print(a)


