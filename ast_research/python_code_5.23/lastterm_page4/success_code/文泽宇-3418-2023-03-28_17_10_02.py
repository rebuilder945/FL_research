def maxsum(SB):
    sorted_SB = sorted(SB)
    AAA = sorted_SB[::2]
    SB = sum(AAA)
    return(SB)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

