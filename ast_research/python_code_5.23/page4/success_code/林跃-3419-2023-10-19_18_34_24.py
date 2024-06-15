def calDegrees(nums):
    dic={}
    for i in nums:
        if i in nums:
            dic[i]=dic[i]+1
        else:
            dic[i]=0
    return max(dic.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

