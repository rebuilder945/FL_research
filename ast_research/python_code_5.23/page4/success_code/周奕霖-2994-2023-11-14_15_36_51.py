a = list(eval(input()))
n,m = eval(input())
v =[]
if -len(a)-1 <= n <= len(a):
    v.append(a[n])
    c = a + v*m
    print(c)
else:
    print("error")
