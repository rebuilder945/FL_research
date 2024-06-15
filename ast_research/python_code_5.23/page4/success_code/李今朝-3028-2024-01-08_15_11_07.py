n,m,l=map(int,input().split(','))
z=n+l*(m-1)
all=[x for x in range(n,z+1,l)]
print(all)
