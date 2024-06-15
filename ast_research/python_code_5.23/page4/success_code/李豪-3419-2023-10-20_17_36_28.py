def calDegrees(nums=[]):
     temp=set(nums)
     d=0
     for i in nums :
         time=nums.count(i)
         if time > d:
            d = time
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

