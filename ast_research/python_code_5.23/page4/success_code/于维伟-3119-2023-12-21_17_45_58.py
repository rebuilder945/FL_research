a=eval(input())
b=a.copy()
for x in b:
    c=a.count(x)
    if c>=2:
        for i in range(c-1):
            a.remove(x)
print(a)
