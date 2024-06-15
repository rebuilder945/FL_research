def maxsum(nums):
    nums.sort()
    numbers=nums[0:len(nums):2]
    return sum(numbers)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

