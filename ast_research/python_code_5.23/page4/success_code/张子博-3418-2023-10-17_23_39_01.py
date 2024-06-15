def maxsum(nums):
    n=int(len(nums)/4)
    nums.sort()
    p=0
    for i in nums[0:n+1]:
        p+=i
    for k in nums[n+1:n*3]:
        p+=k
    return p 





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

