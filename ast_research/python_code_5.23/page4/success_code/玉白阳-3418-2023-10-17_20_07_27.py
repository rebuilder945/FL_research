def maxsum(nums):
    sorted_nums=sorted(nums)
    return sum([nums[i] for i in range(len(nums)) if i%2==0])




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

