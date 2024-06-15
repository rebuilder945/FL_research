a=eval(input())
ma=max(a)
mi=min(a)
for i in a:
    x=a.count(i)
    if i==ma and x!=1:
        a.remove(i)
    elif i==mi and x!=1:
        a.remove(i)
    else:
            continue
print(a)
