a = list(eval(input()))
n,m = eval(input())
if -len(a)<= n <= len(a):
    t = 0
    while t <= m-1:
        t = t+1
        a.append(a[n])
    print(a)
else:
    print("error")


