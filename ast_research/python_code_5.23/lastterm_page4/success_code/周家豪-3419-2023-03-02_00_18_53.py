nums1=[]
def calDegrees(nums):
    for i in nums:
        a=nums.count(i)
        nums1.append(a)
    nums=max(nums1)
    return(nums)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

