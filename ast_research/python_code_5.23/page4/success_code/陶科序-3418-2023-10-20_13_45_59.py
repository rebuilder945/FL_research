def maxsum(nums):
    for i in nums:
        for j in nums:
            if i != j:
                c = i+j
            elif i == j:
                continue
    return(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

