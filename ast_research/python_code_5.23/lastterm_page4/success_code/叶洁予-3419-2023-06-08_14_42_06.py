def calDegree(nums):
    maxc=1
    for x in range(nums):
        a =nums.count(x)
    if a >maxc:
        maxc=a
    return maxc


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

