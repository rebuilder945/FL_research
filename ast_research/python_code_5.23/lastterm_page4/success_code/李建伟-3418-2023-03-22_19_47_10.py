def maxsum(nums):
    lst = nums[-2::-2]
    sum1 = sum(lst)
    return sum1




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

