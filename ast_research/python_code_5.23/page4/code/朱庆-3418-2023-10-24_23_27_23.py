def maxsum(nums):
      n=len(nums)
     c=0
     nums.sort(reverse=True)
     for x in range(1,n+1,2):
           c=c+nums[x]
    return c





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

