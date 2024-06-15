def calDegrees(nums):
    nums=[]
    nums1=[]
    for i in nums:
         a=nums.count(i)
         nums1.append(a)
         n=max(nums1)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

