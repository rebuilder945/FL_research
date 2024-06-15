def maxsum(nums):
    nums.sort()
    x=[[nums[a],nums[a+1]] for a in range(0,len(nums)-1,2)]
    s=0
    for i in x:
        s+=min(i)
    return(s)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

