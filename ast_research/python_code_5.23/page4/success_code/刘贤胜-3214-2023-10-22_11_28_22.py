a=eval(input())
b=a.copy()
for x in b:
    if x==0:
        a.remove(x)
        a.append(x)
print(a)
