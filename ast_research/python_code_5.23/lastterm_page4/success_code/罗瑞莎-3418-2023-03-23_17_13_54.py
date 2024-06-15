def maxsum(nums):
    lst = nums.sort(reverse=True)
    v = lst[len(nums)/2-1]+lst[-1]
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

