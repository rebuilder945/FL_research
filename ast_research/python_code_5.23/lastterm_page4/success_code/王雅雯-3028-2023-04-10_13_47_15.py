n,m,l=map(int,input().strip().split(','))
a=n+(m-1)*l
W=[x for x in range(n,a+1,l)]
print(W)
