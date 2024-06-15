def calDegrees(nums):
    lis=[]
    for i in nums:
        a=nums.count(i)
        lis.append(a)
    return max(lis)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

