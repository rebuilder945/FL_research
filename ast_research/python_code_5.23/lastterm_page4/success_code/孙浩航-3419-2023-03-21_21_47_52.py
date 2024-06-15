def calDegrees(nums):
     
     for i in nums:
         if nums.count(i)>=1:
             list=[nums.count(i)]
         return max(list)
 
    
    
   


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

