def maxsum(nums):
    nums.sort(reverse=True)
    numbers=nums[-1::2]
    return sum(numbers)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

