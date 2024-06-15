n,m=input().split(" ")
n=int(n)
m=int(m)
if n>=m or n<0 or m<0 or m-n<3:
    print("illegal input")
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                s=str(i)+str(j)+str(k)
                if i!=j and i!=k and j!=k and i!=0:
                    print(int(s),end=(" "))

