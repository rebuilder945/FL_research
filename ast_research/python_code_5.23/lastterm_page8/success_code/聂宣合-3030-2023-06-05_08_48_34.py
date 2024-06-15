a=list(input().split(","))
b=list(input().split(","))
b=[eval(s) for s in b ]
sums=list(map(lambda x,y:[x,y],a,b))
sums.sort(key=lambda x :x[-1])
print(sums)
