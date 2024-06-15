def maxsum(nums):
    y = 0
    nums.sort()
    for i in range(len(nums)):
        if i%2==0:
          y+=nums[i];
    return y





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

