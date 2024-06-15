def maxsum(nums):
    nums.sort()
    ls=[x for x in nums[0:len(nums):2]]
    return sum(ls)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

