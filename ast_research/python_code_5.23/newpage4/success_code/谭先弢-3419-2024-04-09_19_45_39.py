def calDegrees(nums):
    A =[]
    for x in nums:
        f = nums.count(x)
        A.append(f)
    m = max(A)
    return m


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

