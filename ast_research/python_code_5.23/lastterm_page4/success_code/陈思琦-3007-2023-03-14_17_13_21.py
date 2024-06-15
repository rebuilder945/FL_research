a=eval(input())
b,c=eval(input())
d=eval(len(a))-1
if c > d or b <0 :
    print("error")
else:
    del a[b:c]
    print(a)
