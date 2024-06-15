def calDegrees(nums):
    dic={}
    for i in nums:
        dic[i]=dic.get(i,0)+1
    lis=[]
    for x,y in dic.items():
        lis.append([x,y])
    lis.sort(key=lambda x:x[1])
    return(lis[-1][1])


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

