a=eval(input())
ma=max(a)
mi=min(a)
for i in a:
    x=a.count(i)
    if i==ma:
        while x!=1:
            a.remove(i)
    elif i==mi:
        while x!=1:
            a.remove(i)
    else:
            continue
print(a)
