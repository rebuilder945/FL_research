n,m=map(int,input().split())
if m-n<3 or m<0 or m>10:
    print('illegal input')
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and k!=i:
                    s=int(str(i)+str(j)+str(k))
                    if s>=100:
                        print(s,end=' ')

