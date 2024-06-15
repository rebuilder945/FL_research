a=eval(input())
b,c=eval(input())
if len(a)>c:
    for x in a[b:c]:
        a.remove(x)
    print(a)
else:
    print("error")
