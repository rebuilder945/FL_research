a=eval(input())
b,c=eval(input())
if b>=len(a):
    print("error")
elif b<len(a):
    d=str(a[b])
    e="".join(d)*c
    a.extend(e)
    print(a)
