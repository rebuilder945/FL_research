a=eval(input())
for x in a:
    if a.count(x)>1:
        for i in range(a.count(x)):
            a.remove(x)
print(a)
