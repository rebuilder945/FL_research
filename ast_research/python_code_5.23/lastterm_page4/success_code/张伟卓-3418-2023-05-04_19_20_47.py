def maxsum(m):
    
    
    m.sort()
    return sum(m[::2])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

