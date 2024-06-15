def maxsum(nums):
    nums.sort()
    result=[]
    for m in range(len(nums)):
        if m%2==0:
            result.append(nums[m])
    a=sum(result)
    return(a)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

