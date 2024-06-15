a=eval(input())
c=[]
for x in a:
    b=a.count(x)
    if b>=2:
        for y in range(b-1):
            a.remove(x)
    else:
        continue
print(a)


