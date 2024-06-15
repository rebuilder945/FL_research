a=eval(input())
b=a.copy()
for i in a:
    if a.count(i)>1:
        if b.count(i)>1:
            b.remove(i)
print(b)
