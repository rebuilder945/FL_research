a=eval(input())
n,m=eval(input())
if n>len(a)-1 or n>m or m<0 or n<0 or m>len(a)-1:
    print("error")
else:
    del a[n:m]
    print(a)
