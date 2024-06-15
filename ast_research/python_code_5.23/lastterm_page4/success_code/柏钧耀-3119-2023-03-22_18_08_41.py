a=input().split(',')
for x in a :
    c=a.count(x)
    if c>1:
        for i in range(c):
            b=a.index(x)
            a.pop(b)
    else:
        None
print(a)
