n,m=map(int,input().split())
jihe=[]
if m-n>2 and m>0 and n>=0:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and j!=k and i!=k:
                    num=i*10**2+j*10+k
                    if 100<num<1000:
                        print(num,end=' ')
                        jihe.append(num)           
if jihe==[]:
    print('illegal input')





