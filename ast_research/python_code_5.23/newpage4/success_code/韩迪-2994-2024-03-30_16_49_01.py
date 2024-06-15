a=list(eval(input()))
n,m=eval(input())
d=len(a)
if n>d-1:
    print("error")
else:
    b=a[n]
    for i in range(m):
        a.append(b)
    print(a)
