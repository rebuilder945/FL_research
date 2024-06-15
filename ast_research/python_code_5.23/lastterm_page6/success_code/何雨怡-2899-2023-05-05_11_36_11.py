n,m=map(int,input().split())
if m-n<3 or n>=m:
    print("illegal input")
elif n<0 and m<0:
    print("illegal input")
else:
    shuzi=[]
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=j and i!=k and j!=k and i!=0:
                    num=100*i+10*j+k
                    if num<1000:
                        shuzi.append(num)
                        print(num,end=" ")
    if shuzi==[]:
        print("illegal input")
