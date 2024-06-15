def maxsum(nums):
    sorted_nums=sorted(nums)
    numbers=nums[0:len(nums):2]
    return sum(numbers)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

