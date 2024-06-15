def calDegrees(nums1)
      a=0
      for x in nums1:
           if nums1.count(x)>a:
               return a+=1


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

