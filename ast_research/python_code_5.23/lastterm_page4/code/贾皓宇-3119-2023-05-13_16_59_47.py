a=eval((input())
for x in a:
    if a.count(x)>1:
        for y in range(a.count(x)-1):
            a.remove(x)
print(a)
