a=list(eval(input()))
ma=max(a)
mi=min(a)
for x in a:
    if x==ma or x==mi:
        a.remove(x)
print(a)
