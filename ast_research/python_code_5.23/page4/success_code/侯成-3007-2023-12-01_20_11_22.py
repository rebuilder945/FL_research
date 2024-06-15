a=eval(input())
b,c=eval(input())
long=int(len(a))
if b>long:
    print("error")
elif c>long:
    print("error")
elif b<=c:
    min=c-b
    while min>0:
        del a[int(b)]
        min-=1
    print(a)
elif b>=c:
    min=b-c
    while min>0:
        del a[int(c+1)]
        min-=1
    print(a)
