def calDegrees(nums):
      D=0
      for i in nums:
           count=nums.count(i)
           if count>D:
                D=count
     return D
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

