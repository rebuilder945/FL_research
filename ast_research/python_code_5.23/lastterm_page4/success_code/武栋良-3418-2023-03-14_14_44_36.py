def maxsum(nums):
    nums.sort()
    for x in nums:
         s = 0
         while nums.index(x) % 2 == 0:
            s = s+x
    return s
  




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

