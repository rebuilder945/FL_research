a=eval(input())
n,m=eval(input())
if n<m:
    a1=a.copy()
    for x in a1[n:m]:
        a.remove(x)
        print(a)
elif n>m:
    print("error")
elif n and m > len(a):
    print("error")
