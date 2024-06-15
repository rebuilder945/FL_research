def maxsum(nums):  
    n = len(nums) // 2  
    pairs = []  
    for i in range(n):  
        pairs.append((nums[i], nums[i+n]))  
    return max(sum(pair) for pair in pairs) 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

