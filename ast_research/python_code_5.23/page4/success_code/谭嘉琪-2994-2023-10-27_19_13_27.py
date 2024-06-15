a=list(eval(input()))
n,m=eval(input())
b=len(a)
if n<0:
    e=-n
else:
    e=n
if e>=b:
    print("error")
else:
    c=a[n]
    for i in range(m):
        a.append(c)
    print(a)
