n = eval(input())
ls = [x for x in range(1,n+1)]
for y in range(0,n-1):
    ls[y],ls[y+1] = ls[y+1],ls[y]
print(ls)
