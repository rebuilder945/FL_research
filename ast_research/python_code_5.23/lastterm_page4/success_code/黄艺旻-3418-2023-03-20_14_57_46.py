def fenge(nums):
    return list(zip(*[iter(sorted(nums))]*2))
nums=fenge(nums)
def maxsum(nums):
     num1 = sum(map(lambda x:x[0],nums))
     return max(num1)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

