def maxsum(nums):
    nums.sort()
    lst = []
    for i in range(len(nums)):
        if i%2 == 0:
            lst.append(nums[i])
    msum = sum(lst)
    return msum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

