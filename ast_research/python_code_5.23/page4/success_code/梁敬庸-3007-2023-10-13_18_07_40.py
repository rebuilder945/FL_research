a=eval(input())
b,c=eval(input())
d=len(a)-1
if b<d and c<d:
    for x in a[b:c]:
        del a[x]
    print(a)
else:
    print("error")
