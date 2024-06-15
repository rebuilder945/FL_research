a=eval(input())
for x in a[:]:
    while a.count(a)>1:
        a.remove(x)
print(a)

