def maxsum(nums):
    
    n=int(len(nums)/2)
    nums.sort()
    sum=0
    for i in range(n):
        sum+=nums[(i)*2]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

