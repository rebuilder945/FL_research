n,m=map(int,input().split(' '))
lst=[]
if  m-n<3:
    print("illegal input")
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z:
                    sanwei=str(x)+str(y)+str(z)
                    lst.append(sanwei)
print(*lst,sep=' ')




    




