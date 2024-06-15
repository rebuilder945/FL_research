a=list(eval(input()))
n,m=eval(input())
if n<len(a):
    b=a[n]
    for x in range(m):
        a.append(b)
    print(a)
else:
    print("error")
