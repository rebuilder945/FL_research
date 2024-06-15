a=eval(input())
b,c=eval(input())
if b and c in a:
    d=len(a[b])
    e=len(a[c]) 
    for x in a[d:e]:
        del a[x]
    print(a)
else:
    print("error")
