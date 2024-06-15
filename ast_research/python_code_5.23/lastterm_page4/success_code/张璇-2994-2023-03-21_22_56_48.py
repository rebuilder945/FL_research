a=eval(input())
b,c=eval(input())
if b>=len(a):
    print("error")
elif b<len(a):
    d=a[b]*c
    a.extend(d)
    print(a)
