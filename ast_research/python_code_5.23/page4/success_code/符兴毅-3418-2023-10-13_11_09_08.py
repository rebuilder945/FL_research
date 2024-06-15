def maxsum(nums):
    nums.sort(reverse=True)
    mix = []
    for i in range(1,len(nums)+1,2):
        mix.append(nums[i])
    return sum(mix)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

