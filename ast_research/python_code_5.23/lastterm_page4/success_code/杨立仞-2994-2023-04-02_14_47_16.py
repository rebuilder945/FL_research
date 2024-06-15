a=eval(input().split(','))
n,m=eval(input())
if n+1>len(a) or (-n)>len(a):
    print("error")
else:
    b=[x**0+int(a[n])-1 for x in range(m)]
    print(a+b)
