l=input().split()
n,m=list(map(int,input().strip().split()))
l[n],l[m]=l[m],l[n]
print(l)
