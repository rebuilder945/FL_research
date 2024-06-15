a=input().split(" ")
b=input().split(" ")
import copy
c=copy.deepcopy(a)
b=list(map(int,b))
n=b[0]
m=b[1]
a[n]=a[m]
a[m]=c[n]
print(a)
