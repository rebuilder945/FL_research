def calDegrees(nums):
    n = eval(nums)
    for i in n:
        if i not in n:
            n[i] = 1
        else:
            n[i] += 1
    return max(n.values())



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

