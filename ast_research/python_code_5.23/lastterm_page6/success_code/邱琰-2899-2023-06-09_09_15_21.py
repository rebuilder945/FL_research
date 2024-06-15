n,m=map(int,input().split())
if n>=m or (m-n)<3:
    print('illegal input')
else:
    s=''
    ls=[]
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and i!=k and j!=k:
                    s=str(i)+str(j)+str(k)
                    if int(s)>=100 and int(s)<=999:
                        ls.append(int(s))
    if len(ls)!=0:
        print(*ls)
    else:
        print('illegal input')

