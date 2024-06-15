a=eval(input())
b,c=eval(input())
d=len(a)
if b<=d:
    for x in range(b,c,1):
        del a[x]
    print(a)
else:
    print("error")
