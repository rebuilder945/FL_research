def maxsum(nums):
    nums.sort()
    a=0
    for x in range(len(nums)):
        if x%2!=0:
            a+=x
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

