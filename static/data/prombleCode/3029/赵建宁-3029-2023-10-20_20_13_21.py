def calDegree(nums):
    value = max(nums)
    for i in range(nums):
        if i == value:
            d += 1
        else:
            d = d
nums = [1,2,3,3,4,5,4,3,3]
d = calDegree(nums)
print(d)
