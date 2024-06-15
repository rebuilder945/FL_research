def maxsum(nums):
    nums=[]
    nums.sort(key=len)
    for m in range(len(nums)):
        if m%2==0:
            result=[]
            result=result.append(nums[m])
    v=sum(result)
    return(v)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

