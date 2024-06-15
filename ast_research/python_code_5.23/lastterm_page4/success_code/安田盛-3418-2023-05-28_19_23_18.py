def maxsum(nums):
    nums.sort()
    a=0
    for x in nums[0:len(nums):2]:
        a+=x
    return(a)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

