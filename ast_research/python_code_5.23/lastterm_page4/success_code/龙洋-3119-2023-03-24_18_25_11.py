lis=eval(input())
for x in lis:
    if lis.count(x)>=2:
        n=lis.count(x)-1
        for a in range(n):
            lis.remove(x)
print(lis)
