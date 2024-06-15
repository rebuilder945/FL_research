def calDegrees(n):
    return max(set(n),key=list.count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

