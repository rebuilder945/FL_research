def calDegrees(nums):
    nums1=nums.copy()
    nums.1sort()
    a=[]
    for i in nums:
        d=nums1.count(i)
        a.append(d)
    return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

