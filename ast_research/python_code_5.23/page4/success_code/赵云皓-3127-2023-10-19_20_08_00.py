n=eval(input())
a=[x for x in range(n)]
for x in a:
    if x==n:
        x=1
    else:
        x=x+1
print(a)
