def maxsum(nums):
    nums=list(nums)
    nums.sort()
    list_2 = nums[::2]
    sum=0
    for i in list_2:
        sum+=i
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

