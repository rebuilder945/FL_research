a=eval(input())
if len(a)<=2:
    print([])
ma=max(a)
mi=min(a)
for i in a:
    if i==ma:
        a.remove(i)
    elif i==mi:
        a.remove(i)
    else:
        continue
print(a)
