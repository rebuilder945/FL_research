a=eval(input())
b=a.copy()
for x in b:
    r=a.count(x)
    if r>=2:
        for i in range(r-1):
            a.remove(x)
print(a)            



