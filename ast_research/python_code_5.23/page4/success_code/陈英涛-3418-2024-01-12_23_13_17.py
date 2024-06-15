def maxsum(nums):
    n=len(nums)
    l=nums.sort(reverse = True)
    c=l[:n:2]
    return(sum(c))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

