def calDegrees(nums):
      dic=[]
      for i in nums:
           b=a.count(i)
           dic.append(b)
      return max(dic.values())   
             


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

