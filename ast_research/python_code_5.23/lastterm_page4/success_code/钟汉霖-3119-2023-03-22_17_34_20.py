a=eval(input())
b=a.copy()
for x in b:
    while a.count(x)>1:
        a.remove(x)
print(a)
