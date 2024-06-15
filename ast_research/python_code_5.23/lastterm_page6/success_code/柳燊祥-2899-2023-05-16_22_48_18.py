n,m=input().split()
if 0<=int(m)<10 and 0<=int(n)<10 and int(m)-int(n)>=3:
    lis=list(range(int(n),int(m)))
    nums=[]
    for i in list(range(int(n),int(m))):
        for j in list(range(int(n),int(m))):
            for k in range(int(n),int(m)):
                if i!=j and j!=k and i!=k and i!=0:
                    nums.append((str(i)+str(j)+str(k)))
    print("".join(str(x)for x in nums))
else:
    print("illegal input")


