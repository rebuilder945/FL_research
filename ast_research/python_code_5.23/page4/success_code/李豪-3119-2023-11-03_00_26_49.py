a=eval(input())
for x in a:
    ge=a.count(x)
    if ge >=2:
        for i in range(ge-1):
            a.remove(x)
print(a)
