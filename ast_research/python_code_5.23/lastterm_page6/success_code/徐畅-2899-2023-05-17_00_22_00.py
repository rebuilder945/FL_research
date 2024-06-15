n,m=map(int,input().split(' '))
lst=[]
if  m-n<3 or n<0 or m>=10:
    print("illegal input")
else:
    for x in range(n,m):
        for y in range(n,m):
            for z in range(n,m):
                if x!=y and x!=z and y!=z and x!=0:
                    sanwei=str(x)+str(y)+str(z)
                    lst.append(sanwei)
print(*lst,sep=' ')




    




