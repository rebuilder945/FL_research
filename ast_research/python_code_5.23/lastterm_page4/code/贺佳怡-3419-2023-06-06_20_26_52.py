def calDegrees(nums1)
      a=nums1.count(nums1[0])
      for x in nums1:
           if nums1.count(x)>a:
               a=nums1.count(x)
     return a
              


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

