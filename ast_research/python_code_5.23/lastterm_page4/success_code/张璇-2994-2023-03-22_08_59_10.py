a=list(eval(input()))
b,c=eval(input())
if b>=len(a):
    print("error")
elif b<len(a):
    d=a[b]
    for e in range(c):
        a.append(d)
    print(a)
