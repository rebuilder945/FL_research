a=eval(input())
b,c=eval(input())
if b and c in a:
    d=a.index(b)
    e=a.index(c) 
    for x in a[d:e]:
        del a[x]
    print(a)
else:
    print("error")
