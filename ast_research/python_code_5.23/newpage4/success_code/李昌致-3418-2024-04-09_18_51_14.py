def maxsum(nums):
    list = []
    nums.sort()
    for i in range(0,len(nums),2):
        list.append(nums[i])
    total = sum(list)
    return total
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

