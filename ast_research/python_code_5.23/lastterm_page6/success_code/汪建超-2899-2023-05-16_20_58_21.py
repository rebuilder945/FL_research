n,m = map(int,input().split())
lst = []
if n > m or m-n<3 or n<0:
    print("illegal input") 
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and z!=x:
                    s = 100*x+y*10+z
                    lst.append(s)
print(*lst)
