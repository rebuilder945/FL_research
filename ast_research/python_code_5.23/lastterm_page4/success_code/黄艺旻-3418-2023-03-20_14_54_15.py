def fenge(nums):
    return list(zip(*[iter(sorted(nums))]*2))

def maxsum(nums):
    return sum(map(lambda x:x[0],nums))
nums=fenge(nums)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

