a=eval(input())
for x in range(len(a)-1,-1,-1):
    if a.count(a[x])>1:
        a.pop(x)
print(a)
