def calDegrees(l1:list[]):
      return max(set(l1),key(l1.count))
      
     


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

