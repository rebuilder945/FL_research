a=eval(input())
n,m=eval(input())
if n<m:
    a1=a.copy()
    for x in a[n:m]:
        a.remove(x)
        print(a1)
elif n>m:
    print("error")
elif n and m > len(a):
    print("error")

