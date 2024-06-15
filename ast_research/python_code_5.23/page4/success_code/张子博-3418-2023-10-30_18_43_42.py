def maxsum(nums):
    n=int(len(nums)/2)
    nums.sort()
    p=0
    for i in nums[0::2]:
          p+=i
    return p    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

