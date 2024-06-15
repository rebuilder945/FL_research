a=eval(input())
n,m=eval(input())
if  m<0 or n<0:
    print("error")
elif n>len(a)-1 or n>len(a)-1: 
    print("error")
elif   n<m:
    del a[n:m]
    h=a
    print(h)
elif    m>n:
     del a[m:n]
     h=a
     print(h)
else:
    print("error")






