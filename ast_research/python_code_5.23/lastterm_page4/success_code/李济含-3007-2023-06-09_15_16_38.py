a=eval(input())
n,m=map(int,input().split(","))
if n<a[0] or n>a[-1] or m<a[0] or m>a[-1] or n>m :
    print("erroe")
else:
    print(a[0:n]+a[m:])

