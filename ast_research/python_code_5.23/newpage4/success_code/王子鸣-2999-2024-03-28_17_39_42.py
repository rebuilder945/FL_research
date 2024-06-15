a1=list(map(str,input().split(" ")))
n,m=list(map(int,input().split(" ")))
temp=a1[n]
a1[n]=a1[m]
a1[m]=temp
print(a1)
