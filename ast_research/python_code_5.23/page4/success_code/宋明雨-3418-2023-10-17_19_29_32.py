def maxsum(nums):
    A = len(nums)
    nums.sort()
    List1 = nums[0:A+1]
    List2 = nums[A+1: ]
    a,b=min(List1),min(List2)
    return a + b 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

