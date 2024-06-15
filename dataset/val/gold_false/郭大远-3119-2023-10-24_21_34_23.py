a=eval(input())
for x in a:
    while a.count(x)>1:
        a.remove(x)
print(a)

