def maxsum(nums):
    nums.sort()
    n2=[]
    for x in nums[0::2]:
        n2.append(x)
    return sum(n2)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

