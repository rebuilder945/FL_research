a=eval(input())
b,c=eval(input())
d=len(a)
if b<d and c<d:
    for x in a[b:c]:
        del a[x]
    print(a)
else:
    print("error")
