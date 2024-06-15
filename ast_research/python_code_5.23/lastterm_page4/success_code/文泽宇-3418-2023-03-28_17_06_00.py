def maxsum(SB):
    sorted_SB = sorted(SB)
    AAA = sorted_SB[::1]
    print(sum(AAA))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

