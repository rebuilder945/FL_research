def maxsum(nums):
    import random
    random.shuffle(nums)
    max_ = 0
    for i in range(0,len(nums),2):
        max_  += max(nums[i],nums[i+1])
        return sum(max_)
       
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

