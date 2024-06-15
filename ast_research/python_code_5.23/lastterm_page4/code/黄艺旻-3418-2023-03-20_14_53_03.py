def fenge(nums):
    return list(zip(*[iter(sorted(nums))]*2))

def maxsum(fenge_nums):
    return sum(map(lambda x:x[0],fenge_nums))
fenge_nums=fenge(nums)
maxsum(nums)=maxsum(fenge_nums)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

