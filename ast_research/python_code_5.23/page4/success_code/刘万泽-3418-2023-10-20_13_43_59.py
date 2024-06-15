def maxsum(nums):
    t=[]
    for a in nums:
        for b in nums:          
            t.append(a+b)
    return max(t)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

