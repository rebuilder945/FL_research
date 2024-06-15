n,m=input().split()
sums=[]
if 0<=int(n)<10 and 0<=int(m)<10 and int(m)-int(n)>=3:
    for i in list(range(int(n),int(m))):
        for j in list(range(int(n),int(m))):
            for k in list(range(int(n),int(m))):
                if i!=j and j!=k and k!=i and i!=0:
                    sums.append(str(i)+str(j)+str(k))
    print("".join(str(x) for x in sums))
else:
    print("illegal input")
