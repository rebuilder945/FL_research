a=eval(input())
b,c=eval(input())
if b>c:
    print("error")
else:
    del a[b:c]
    print(a)
