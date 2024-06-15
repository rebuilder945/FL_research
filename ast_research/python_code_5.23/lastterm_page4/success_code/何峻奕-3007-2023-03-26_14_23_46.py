a=eval(input())
n,m=eval(input())
if n<m:
    a1=a.copy()
    for x in range(n,m):
        a.remove(x)
    print(a1)
if n>m:
    print("error")
elif n or m > len(a):
    print("error")

