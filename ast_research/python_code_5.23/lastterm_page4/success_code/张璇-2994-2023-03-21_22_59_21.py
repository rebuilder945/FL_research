a=eval(input())
b,c=eval(input())
if b>=len(a):
    print("error")
elif b<len(a):
    d=a[b]
    e=list(d)*c
    a.append(e)
    print(a)
