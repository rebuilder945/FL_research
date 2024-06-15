def maxsum(nums):
    nums.sort()
    n=len(nums)//2
    maxsum=sum(nums[1] for i in range (n,2*n))
    return max(maxsum,sum(nums[:n]))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

