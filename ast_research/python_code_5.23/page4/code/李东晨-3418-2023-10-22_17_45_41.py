def maxsum(nums):
    nums.sort()
    a=nums[0:len(nums):2]
    b=sum(a)
    retyrn b




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

