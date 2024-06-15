a=eval(input())
max=max(a)
min=min(a)
while max in a:
    a.remove(max)
while max in a:
    a.remove(min)
print(a)
