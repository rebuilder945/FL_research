ls=list(map(int,input().split(',')))
print([i for i in range(ls[0],ls[2]*ls[1]+ls[0],ls[2])])
