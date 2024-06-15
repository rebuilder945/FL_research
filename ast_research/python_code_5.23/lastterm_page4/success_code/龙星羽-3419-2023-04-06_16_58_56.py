def calDegrees(nums):
    du=[1 for x in range(max(nums))]
    for x in nums:
        if du[x-1]<nums.count(x) :
            du[x-1]+=1
    return max(du)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

