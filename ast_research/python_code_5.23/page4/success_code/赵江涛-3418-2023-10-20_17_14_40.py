def maxsum():
    nums.sort()
    nums.reverse()
    a = nums[1]
    b = nums[3]
    v = a+b
    return v





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

