n,m=map(int,input().split())
if 0<=n<m<11 and m-n>=3:
    ls=[]
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and y!=z and z!=x:
                    s=str(x)+str(y)+str(z)
                    s1=int(s)
                    if 99<s1<1000 and s1 not in ls:
                        ls.append(s1)
    ls1=[str(i) for i in ls] 
    print(' '.join(ls1)) 
else:
    print('illegal input')              
