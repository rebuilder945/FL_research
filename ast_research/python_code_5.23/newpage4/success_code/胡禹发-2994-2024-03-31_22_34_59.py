a=list(eval(input()))
b=a.copy()
n,m=eval(input())
for i in a:
    if i==a[n]:
        for i in range(m):
            b.append(a[n])
        print(b)
if b==a:
    print("error")
