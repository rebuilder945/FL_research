a=eval(input())
n,m=eval(input())
if  n>len(a)-1 and m>len(a)-1:
    print("error")
elif   n<m:
    del a[n:m]
    h=a
    print(h)
elif   n>m:
    print("error")
else:
    print("error")

