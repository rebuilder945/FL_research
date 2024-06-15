a=eval(input())
b,c=eval(input())
d=len(a)
if b>=c or b>=d:
    print("error")
else:
    del a[b:c]
    print(a)

