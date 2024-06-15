i=input().split()
n,m=map(int,input().split())
a=i[n]
i[n]=i[m]
i[m]=a
print(i)
