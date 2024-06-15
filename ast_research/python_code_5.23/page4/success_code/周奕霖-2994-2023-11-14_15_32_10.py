a = list(eval(input()))
n,m = eval(input())
if -len(a)-1 <= n <= len(a):
    b = list(a[n])*m
    c = a + b
else:
    print("error")
