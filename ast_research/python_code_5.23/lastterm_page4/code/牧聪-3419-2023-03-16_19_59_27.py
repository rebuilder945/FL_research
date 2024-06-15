delDegrees(a):
counts = {}
degree = 0
for num in nums:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
    degree = max(degree, counts[num])
return degree


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

