# 组合数字
n,m=map(int,input().split())
if 0<m<10 and 0<=n<10 and (m-n) >= 3:
    lis=[x for x in range(n,m)]
    nums=[]
    for i in lis:
        for j in lis:
            for k in lis:
                if i!= j and j != k and i != k and i != 0:
                    nums.append(str(i)+str(j)+str(k))
    # print(" ".join(str(x) for x in nums))
    print(" ".join(nums))
    # save=[]
    # for x in nums:
    #     if x not in save:
    #         save.append(x) 
    # print(" ".join(save))
else:
    print("illegal input")
