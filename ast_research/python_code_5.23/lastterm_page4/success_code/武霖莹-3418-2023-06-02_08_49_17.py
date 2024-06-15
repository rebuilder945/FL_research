def maxsum(nums):
    nums.sort()
    lst = nums[-2::-2]
    sums = sum(lst)
    return(sums)
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

