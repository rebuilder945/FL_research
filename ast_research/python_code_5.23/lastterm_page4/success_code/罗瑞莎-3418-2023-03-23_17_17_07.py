def maxsum(nums):
    lst = nums.sort(reverse=True)
    a = len(nums)/2
    v = lst[int(a)-1]+lst[-1]
    return v




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

