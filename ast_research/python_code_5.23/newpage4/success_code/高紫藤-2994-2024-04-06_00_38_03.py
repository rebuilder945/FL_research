a = list(eval(input()))
n,m = input().split()
n = int(n)
m = int(m)
if n <= len(a):
    b = a[n]
    a.extend([b]*m)
    print(a)
if n > len(a):
    print("error")




