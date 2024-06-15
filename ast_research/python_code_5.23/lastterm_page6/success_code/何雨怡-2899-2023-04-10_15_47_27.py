n,m=map(int,input().split())
if n>=m:
    print('illegal input')
elif m-n<=2:
    print('illegal input')
elif n<0:
    print('illegal input')
elif m<0:
    print('illegal input')
elif n%1!=0 or m%1!=0:
    print('illegal input')
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and i!=k:
                    num=i*10**2+j*10+k
                    if num<=100:
                        pass
                    elif num>=1000:
                        pass
                    else:
                        print(num,end=' ')



