def maxsum(nums):
    nums.sort()
    a=nums[ :  :2]
    return(sum(a))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

