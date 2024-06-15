# 组合数字
# n,m=map(int,input().split())

# if (n-m)>=3 and 0<=n<10 and 0<m<10:
#     lst=[ x for x in range(n,m)]
# #     nums=[]
# #     for i in lst:
# #         for j in lst:
# #             for k in lst:
# #                 if i!= j and j != k and i != k and i != 0:
# #                     nums.append(str(i)+str(j)+str(k))   
# #                     print(" ".join(str(x) for x in nums))
# # else:
# #     print("illegal input")








n,m=input().split()
if 0<=int(m)<10 and 0<=int(n)<10 and int(m)-int(n) >= 3:
    lis=list(range(int(n),int(m)))
    nums=[]
    for i in lis:
        for j in lis:
            for k in lis:
                if i!= j and j != k and i != k and i != 0:
                    nums.append(str(i)+str(j)+str(k))
    print(" ".join(str(x) for x in nums))
else:
    print("illegal input")

