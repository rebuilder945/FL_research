def maxsum(nums):
    nums.sort(reverse=True)
    n=len(nums)
    b=[]
    for i in range(1,n,2):
        b.append(nums[i])
    c=sum(b)
    return c




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

