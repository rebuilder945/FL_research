def calDegrees(nums):
    nums=list(nums)
    nums.sort()
    for i in range(len(nums)):
        a = nums.count(nums[i])
        nums.append(a)
        del nums[:a-1]
    nums=max(nums)
    return(nums)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

