def calDegrees(nm):
    nm=set(nums)
    nums1=[]
    for i in nm:
         a=nums.count(i)
         nums1.append(a)
         n=max(nums1)
         return n



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

