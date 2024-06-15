def maxsum(nums):
    nums.sort()
    n=nums[0:len(nums):2]
    s=sum(n)
    return s
    nums  =  eval(input())




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

