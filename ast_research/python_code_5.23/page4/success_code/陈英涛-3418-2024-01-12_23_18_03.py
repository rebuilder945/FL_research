def maxsum(nums):
    n=len(nums)
    nums.sort(reverse = True)
    c=nums[:n:2]
    return(sum(c))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

