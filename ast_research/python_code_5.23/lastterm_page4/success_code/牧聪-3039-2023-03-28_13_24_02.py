a=eval(input())
max=max(a)
while max in a:
    a.remove(max)
min=min(a)
while min in a:
    a.remove(min)
print(a)
