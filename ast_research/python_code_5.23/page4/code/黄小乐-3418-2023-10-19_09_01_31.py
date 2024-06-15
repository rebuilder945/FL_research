def maxsum(nums):
    nums = nums.sort(key=len)
    for m in nums in range(2n):
        if m%2==0:
            result=sum(result.append(m))
    return(result)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

