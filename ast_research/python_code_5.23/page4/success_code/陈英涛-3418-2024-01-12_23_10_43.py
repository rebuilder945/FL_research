def maxsum(nums):
    nuums=nums.sort(reverse = True)
    n=len(nums)+1
    c=nums[:n:2]
    return(sum(c))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

