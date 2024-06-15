a=list(input().split(","))
b=list(input().split(","))
b=[eval(x) for x in b]
print(b)
sums=list(map(lambda x,y: [x,y],a,b))
print(sums)
