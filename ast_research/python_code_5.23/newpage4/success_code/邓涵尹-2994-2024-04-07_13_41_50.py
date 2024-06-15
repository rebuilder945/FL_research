a=list(eval(input()))
n,m=eval(input())
r=len(a)
if abs(int(n)) < r and int(n) > 0:
    a = 0
    while a < int(m):
        a.append(a[int(n)])
        a = a+1
    print(a)
elif abs(int(n)) < r and int(n) <0:
    b = 0
    while b < int(m):
        a.append(a[int(n)+r])
        b = b+1
    print(a)
else:
    print("error")
