def calDegress(nums):
    degress = []
    for x in nums:
       degress.append(nums.count(x))
    degress.sort()
    return degress[-1]


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

