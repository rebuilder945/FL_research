a=eval(input())
b,c=eval(input())
if b and c in a:
    for x in a[b,c]:
        del a[x]
    print(a)
else:
    print("error")
