def maxsum(nums):
    nums.sort()
    ww=[x for x in nums[0:-1:2]]
    return(sum(ww))

    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

