def calDegrees(a):
    b = []
    for x in nums:
          b.append(nums.count(x))
    c=max(b)
    return c  


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

