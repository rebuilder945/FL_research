a = eval(input())
b,c = eval（input())
if b==c:
    print(a)
elif b>c:
    if b<len(a):
    
        del a[c+1:b+1]
        print(a)
    else:
        print("error")
elif b<c:
    if c<len(a):
        del a[b:c]
        print(a)
    else:
        print("error")
else:
    print("error")
