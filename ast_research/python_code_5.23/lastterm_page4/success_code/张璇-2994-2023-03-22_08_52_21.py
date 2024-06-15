a=list(eval(input()))
b,c=eval(input())
if b>=len(a):
    print("error")
elif b<len(a):
    d=str(a[b])
    e=",".join(d)*c
    f=[int(x)for x in e]
    a.extend(f)
    print(a)
