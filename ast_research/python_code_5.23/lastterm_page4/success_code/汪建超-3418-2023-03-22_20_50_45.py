def maxsums(nums):
    sums.sort()
    new=sums[0:len(sums):2]
    he=sum(new)
    return he




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

