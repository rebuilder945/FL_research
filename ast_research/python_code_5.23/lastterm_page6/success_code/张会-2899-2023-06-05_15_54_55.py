n,m=map(int,input().split())
if n<0 or m<0 or n>=m or m-n<3:
    print('illegal input')
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and z!=x:
                    s=str(x)+str(y)+str(z)
                    print(s,end=' ')
    
