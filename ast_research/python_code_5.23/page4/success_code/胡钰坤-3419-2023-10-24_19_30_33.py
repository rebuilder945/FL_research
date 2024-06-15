def calDegrees(nums):
    nums2 = []
    for i in nums:
        nums2+=nums
        if i in nums2:
            n = n +1
    return n
            


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

