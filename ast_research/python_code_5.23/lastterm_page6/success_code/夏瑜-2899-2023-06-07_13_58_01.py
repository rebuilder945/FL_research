n,m=map(int,input().split())
list=[]
if type(n) !=int or type(m)!=int or (m-n)<3:
    print("illegal input")
else:
        for i in range(n,m):
            for j in range(n,m):
                for k in range(n,m):
                    if i!=j and j!=k and i!=k and i!=0:
                        list.append(str(i)+str(j)+str(k))
print(' '.join(list))
                    

