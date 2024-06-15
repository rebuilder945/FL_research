a=eval(input())
for b in range(len(a)-1,-1,-1):
    if a.count(a[b])>1:
        a.pop(b)
print(a)
