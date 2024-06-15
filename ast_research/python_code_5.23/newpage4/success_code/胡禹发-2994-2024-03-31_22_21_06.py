a=list(eval(input()))
b=a.copy()
n,m=eval(input())
if n in range(len(a)):
    for i in range(m):
        b.append(a[n])
    print(b)
else:
    print("error")
