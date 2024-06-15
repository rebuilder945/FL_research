a=eval(input())
b,c=eval(input())
d=(len(a))-1
if c > d or b > d :
    print("error")
else:
    del a[b:c]
    print(a)
