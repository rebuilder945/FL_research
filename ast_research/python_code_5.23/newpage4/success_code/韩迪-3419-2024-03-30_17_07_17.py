def  calDegrees(nums):
       max_degree=0
       for x in nums:
              if nums.count(x)>max_degree:
                     max_degree=nums.count(x)
                    
                     return (max_degree)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

