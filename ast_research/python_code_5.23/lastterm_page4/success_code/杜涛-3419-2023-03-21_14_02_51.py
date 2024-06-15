def calDegress():
    m = 0
    for i in nums:
        n = nums.count(i)
        if n>m:
            m = n
    return m


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

