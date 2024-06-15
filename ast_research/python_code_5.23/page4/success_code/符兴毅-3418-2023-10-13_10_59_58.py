def maxsum(nums):
    nums.sort(reverse=False)
    mix = [values for values in range(1,len(nums)+1,2)]
    return sum(mix)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

