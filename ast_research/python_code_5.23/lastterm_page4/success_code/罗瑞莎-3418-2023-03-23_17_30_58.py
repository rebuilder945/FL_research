def maxsum(nums):
    lst = nums.sort(reverse=False)
    sum = 0
    for i in range(len(nums)):
        if i%2 == 0:
            sum+=lst[i]
    return sum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

