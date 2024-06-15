a = eval(input())
n,m,sum=2,1,0
for i in range(a):
    sum=sum+n/m
    n,m=m+n,n
print("{:.4f}".format(sum))
