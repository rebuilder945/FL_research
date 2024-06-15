def calDegrees(N):
    MMM=0
    for x in range(len(N)):
        if N.count(N[x]) > MMM:
            MMM=N.count(N[x])
            return MMM


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

