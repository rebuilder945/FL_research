def calDegrees(nums):
       nums  =  eval(input())
       a=[]
       for i in range(nums):
            if i not in nums:
               a=[1]
            if i in nums:
               a=a+1
        print(max(a.values()))
          
                
       


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

