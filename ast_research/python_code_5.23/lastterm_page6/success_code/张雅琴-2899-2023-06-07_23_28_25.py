n,m=map(int,input().split())
if n>=m or m-n<3 or m<0 or n<0 or n>=10 or m>10:
    print("illegal input")
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and z!=x and x!=0:
                    print(str(x)+str(y)+str(z),end=' ')
