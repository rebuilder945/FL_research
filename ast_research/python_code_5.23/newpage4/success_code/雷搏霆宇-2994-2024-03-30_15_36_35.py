a = list(eval(input()))
b = []
b = a.copy()
n,m = eval(input())
if -len(a)<= n <= len(a):
    t = 0
    while t <= m-1:
        t = t+1
        b.append(a[n])
    print(b)
else:
    print("error")


