n,m=input().split()
if int(n)<int(m) and int(m)-int(n)==3:
    for i in range(n,m):
        for j in range(n,m):
            for x in range(n,m):
                if i!=j and j!=x and i!=x:
                    print(i,j,x)
else:
    print('illegal input')
