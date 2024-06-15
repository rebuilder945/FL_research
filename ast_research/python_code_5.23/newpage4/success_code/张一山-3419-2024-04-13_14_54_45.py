def calDegrees(N):
    MMM=0
    for x in N:
        if N.count(x) > MMM:
            MMM=N.count(x)
            return MMM


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

