a=eval(input())
ma=max(a)
mi=min(a)
for i in a:
    if i==ma or mi:
        a.remove(i)
print(a)
