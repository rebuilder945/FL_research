a=eval(input())
for x in a:
    if x==0:
        a.remove(x)
        a.append(x)
print(a)
