def maxsum(nums):
    import random
    random.shuffle(nums)
    return sum(max(nums)[::len(nums)/2])
       
    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

