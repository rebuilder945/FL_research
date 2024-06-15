n,m=map(int,input().split())
list=[]
if type(n) !=int or type(m)!=int or (m-n)<3:
    print("illegal input")
else:
        for i in range(n,m):
            for j in range(i+1,m):
                for x in range(i+2,m):
                    while i+2<m:
                        if i!=0:
                            z=str(i)+str(j)+str(x)
                            list.append(z)
                        else:
                            break
                    else:
                        break

