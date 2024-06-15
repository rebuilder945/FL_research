def calDegrees(nums):
    nums=list(nums)
    for i in range(len(nums)):
        a = nums.count(nums[i])
        del nums[i]
        nums.append(a)
    nums=max(nums)
    return(nums)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

