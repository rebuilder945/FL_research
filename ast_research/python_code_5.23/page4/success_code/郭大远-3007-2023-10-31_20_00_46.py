a=eval(input())
n,m=eval(input())
if n>len(a)-1 or m>len(a)-1: 
    print("error")
elif   n<m:
    del a[n:m]
    h=a
    print(h)
elif    n>m:
     del a[m:n]
     h=a
     print(h)
else:
    print("error")






