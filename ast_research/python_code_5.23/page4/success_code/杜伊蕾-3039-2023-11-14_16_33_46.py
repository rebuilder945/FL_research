a=eval(input())
for x in range(a.count(max(a))):
    a.remove(max(a))
for x in range(a.count(min(a))):
    a.remove(min(a))
print(a)
