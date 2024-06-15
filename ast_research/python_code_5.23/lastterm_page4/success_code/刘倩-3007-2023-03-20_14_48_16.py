a = eval(input())
n,m = map(int,input().split(','))

if n<0 or m>len(a) or n>m:
    print("error")
else:
    del a[n:m]
    print(a)
