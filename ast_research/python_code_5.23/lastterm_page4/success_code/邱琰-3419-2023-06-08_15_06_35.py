def calDegrees(nums):
    ls=[]
    for i in range(len(nums)):
        ls.append(nums.count(nums[i]))
        return max(ls)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

