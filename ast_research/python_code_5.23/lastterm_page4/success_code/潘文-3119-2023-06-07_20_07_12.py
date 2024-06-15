a=eval(input())
b=a.copy()
for i in a:
    c=b.count(i)
    if c>1:
        while c>1:
            b.remove(x)
            c-=1
print(b)
