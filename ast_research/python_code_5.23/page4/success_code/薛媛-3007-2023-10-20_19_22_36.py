a=eval(input())
n,m=map(int,input().split(','))
if n >= len(a):
    print("error")
else:
    del a[n:m]
    print(a)
