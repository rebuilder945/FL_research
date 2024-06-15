a=eval(input())
for x in a[:]:
    while a.count(a)>0:
        a.remove(x)
print(a)

