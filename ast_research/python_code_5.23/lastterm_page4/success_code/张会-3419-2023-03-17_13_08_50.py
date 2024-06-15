def calDegrees(nums):
    nums = ()
    for i in nums:
        if i not in nums:
            n[i] = 1
        else:
            n[i] += 1
    return max(n.values())



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

