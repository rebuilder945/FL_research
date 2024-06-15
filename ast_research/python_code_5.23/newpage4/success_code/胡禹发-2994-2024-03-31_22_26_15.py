a=list(eval(input()))
b=a.copy()
n,m=eval(input())
for i in range(len(a)):
    if n == a[i]:
        for i in range(m):
            b.append(a[n])
        print(b)
else:
    print("error")
